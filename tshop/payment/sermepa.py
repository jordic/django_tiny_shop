#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ^ la línia superior serveix per poder posar accents a l'arxiu
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
""" 

"""
from sermepa.forms import SermepaPaymentForm
from django.conf import settings
from django.core.urlresolvers import reverse

def sermepa_form(order):
    
    merchant_url = "http://%s%s" % (settings.SITE_DOMAIN, reverse('sermepa_ipn'))
    
    sermepa_dict = {
        "Ds_Merchant_Titular":              settings.SERMEPA_TITULAR,
        "Ds_Merchant_MerchantData":         settings.SERMEPA_MERCHANTDATA,
        "Ds_Merchant_MerchantName":         settings.SERMEPA_MERCHANTNAME,
        "Ds_Merchant_ProductDescription":   settings.SERMEPA_PRODUCTDESCRIPTION,
        "Ds_Merchant_Amount":               order.total(),
        "Ds_Merchant_TransactionType":      settings.SERMEPA_TRANSACTIONTYPE,
        "Ds_Merchant_Terminal":             settings.SERMEPA_TERMINAL,
        "Ds_Merchant_MerchantCode":         settings.SERMEPA_MERCHANTCODE,
        "Ds_Merchant_Order":                order.uid,
        "Ds_Merchant_Currency":             settings.SERMEPA_CURRENCY,
        "Ds_Merchant_MerchantURL": merchant_url,
        "Ds_Merchant_UrlOK": "http://%s%s" % (settings.SITE_DOMAIN, reverse('return_url')),
        "Ds_Merchant_UrlKO": "http://%s%s" % (settings.SITE_DOMAIN, reverse('cancel_url')),
    }
    
    form = SermepaPaymentForm(initial=sermepa_dict)
    if settings.DEBUG:
        rendered_form = form.sandbox()
    else:
        rendered_form = form.render()
    return rendered_form