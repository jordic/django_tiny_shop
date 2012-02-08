#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ^ la línia superior serveix per poder posar accents a l'arxiu
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
""" 

"""

from django.conf import settings
from django.core.urlresolvers import reverse
from sermepa.forms import SermepaPaymentForm
from sermepa.signals import payment_was_successful, payment_was_error, signature_error
from order.models import Order
from order.views import email_notification
from decimal import *

def sermepa_form(order):
    
    merchant_url = "%s%s" % (settings.SITE_DOMAIN, reverse('sermepa_ipn'))
    
    sermepa_dict = {
        "Ds_Merchant_Titular":              settings.SERMEPA_TITULAR,
        "Ds_Merchant_MerchantData":         settings.SERMEPA_MERCHANTDATA,
        "Ds_Merchant_ProductDescription":   "Pedido %s" % (order.uid),
        "Ds_Merchant_Amount":               str(order.total()).replace(".", ""),
        "Ds_Merchant_TransactionType":      settings.SERMEPA_TRANSACTIONTYPE,
        "Ds_Merchant_Terminal":             settings.SERMEPA_TERMINAL,
        "Ds_Merchant_MerchantCode":         settings.SERMEPA_MERCHANTCODE,
        "Ds_Merchant_Order":                order.uid,
        "Ds_Merchant_Currency":             settings.SERMEPA_CURRENCY,
        # Ds_Merchant_ConsumerLanguage
        "Ds_Merchant_MerchantURL": merchant_url,
        "Ds_Merchant_UrlOK": "%s%s" % (settings.SITE_DOMAIN, reverse('return_url')),
        "Ds_Merchant_UrlKO": "%s%s" % (settings.SITE_DOMAIN, reverse('cancel_url')),
    }
    

    form = SermepaPaymentForm(initial=sermepa_dict)
    if settings.DEBUG:
        rendered_form = form.sandbox()
    else:
        rendered_form = form.render()
    return rendered_form


def confirm_payment(sender, **kwargs):
        print sender
        try:
            order = Order.objects.get(uid=sender.Ds_Order)
        except:
            return
        #order = Order.objects.get(uid=sender.invoice)
        order.status = Order.PAYED
        order.pay_date = sender.creation_date
        a = str(sender.Ds_Amount) #".".join((str(p)[:-2],str(p)[-2:]))
        order.pay_total = ".".join( (a[:-2],a[-2:]) )
        order.pay_id = sender.Ds_AuthorisationCode
        order.save()
        email_notification(order)
    
    
#payment_was_successful
payment_was_successful.connect(confirm_payment)