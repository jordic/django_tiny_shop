#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ^ la línia superior serveix per poder posar accents a l'arxiu
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
""" 

"""

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

import hashlib

from models import SermepaResponse

class SermepaPaymentForm(forms.Form):

    Ds_Merchant_Currency = forms.IntegerField(widget=forms.HiddenInput())
    Ds_Merchant_Titular = forms.CharField(widget=forms.HiddenInput())
    Ds_Merchant_MerchantName = forms.CharField(widget=forms.HiddenInput())
    Ds_Merchant_ProductDescription = forms.CharField(widget=forms.HiddenInput())
    Ds_Merchant_MerchantData = forms.CharField(widget=forms.HiddenInput())
    Ds_Merchant_MerchantURL = forms.CharField(widget=forms.HiddenInput())
    Ds_Merchant_TransactionType = forms.IntegerField(widget=forms.HiddenInput())
    Ds_Merchant_Amount = forms.IntegerField(widget=forms.HiddenInput())
    Ds_Merchant_MerchantSignature = forms.CharField(widget=forms.HiddenInput())
    Ds_Merchant_Terminal = forms.IntegerField(widget=forms.HiddenInput())
    Ds_Merchant_MerchantCode = forms.CharField(widget=forms.HiddenInput())
    Ds_Merchant_Order = forms.CharField(widget=forms.HiddenInput())
    Ds_Merchant_UrlOK = forms.CharField(widget=forms.HiddenInput())
    Ds_Merchant_UrlKO = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(SermepaPaymentForm, self).__init__(*args, **kwargs)
        key = '%s%s%s%s%s%s%s' % (self.initial['Ds_Merchant_Amount'], 
                                  self.initial['Ds_Merchant_Order'], 
                                  self.initial['Ds_Merchant_MerchantCode'], 
                                  self.initial['Ds_Merchant_Currency'],
                                  self.initial['Ds_Merchant_TransactionType'], 
                                  self.initial['Ds_Merchant_MerchantURL'],
                                  settings.SERMEPA_SECRET_KEY,)
        sha1 = hashlib.sha1(key)
        self.initial['Ds_Merchant_MerchantSignature'] = sha1.hexdigest().upper()
        
    def render(self):
        return mark_safe(u"""<form action="%s" method="post">
            %s
        """ % (settings.SERMEPA_URL_PRO, self.as_p()))
        
    def sandbox(self):
        return mark_safe(u"""<form action="%s" method="post">
            %s
        """ % (settings.SERMEPA_URL_TEST, self.as_p()))
        
class SermepaResponseForm(forms.ModelForm):
    Ds_Date = forms.DateField(required=False, input_formats=('%d/%m/%Y',))
    Ds_Hour = forms.TimeField(required=False, input_formats=('%H:%M',))

    class Meta:
        model = SermepaResponse
    
