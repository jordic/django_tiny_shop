#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm


def get_payment(order):
    res = {
        'paypal': paypal_form,
        'sanostra': sanostra_form
    }
    return res[order.pay_type](order)


def paypal_form(order):
    res = {}
    paypal = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': order.total(),
        'item_name': settings.PAYPAL_SUBJECT_LINE,
        #'item_number': 1,
        #'quantity':1,
        # PayPal wants a unique invoice ID
        'invoice': order.uid, 
        # It'll be a good idea to setup a SITE_DOMAIN inside settings
        # so you don't need to hardcode these values.
        'currency_code': 'EUR',
        'lc': 'es_ES',
        'notify_url': settings.SITE_DOMAIN + "/tienda/checkout/paypal/ipn",
        'return_url': settings.SITE_DOMAIN + reverse('return_url'),
        'cancel_return': settings.SITE_DOMAIN + reverse('cancel_url'),
    }
    form = PayPalPaymentsForm(initial=paypal)
    if settings.DEBUG:
        rendered_form = form.sandbox()
    else:
        rendered_form = form.render()
    return rendered_form


def sanostra_form(order):
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    