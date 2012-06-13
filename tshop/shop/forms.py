#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
from django import forms
from client.models import Client
from django.conf import settings
from django.forms.widgets import RadioSelect
from django.forms.models import save_instance
from shop.cart import Cart, cart_from_session
from order.models import order_from_cart, Order
from django.shortcuts import get_object_or_404    
from django.contrib.localflavor.es.forms import *
import signals
from django.utils.translation import ugettext_lazy as _

DEFAULT_COUNTRY = getattr(settings, 'DEFAULT_COUNTRY',  'ES')
COUNTRIES = getattr(settings, 'COUNTRIES', ())

class CheckoutForm(forms.ModelForm):
    
    pago = forms.ChoiceField(widget=RadioSelect(), 
        choices=settings.PAYMENT_MODES, initial=settings.PAYMENT_MODES_DEFAULT )

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        #print len(COUNTRIES)
        if len(COUNTRIES) <= 1:
            del self.fields['ship_country']
        signals.checkout_form_created.send(sender=CheckoutForm, form=self)
        
        
    class Meta:
        model = Client
    
    def create_order(self, request, form=None):
        if request.session.get(settings.ORDER_KEY):
            uid = request.session[settings.ORDER_KEY]
            try:
                order = Order.objects.get(uid=uid)
                order.delete()
            except:
                pass
        
        #try to search if contact already exists in database
        try:
            contact = get_object_or_404(Client, email=self.cleaned_data['email'])
            self.instance = contact
            #print "he trobat instancia %s" % self.instance
        except:
            contact = None;
    
        #contact = save_instance(self, contact)
        if self.instance:
            contact = save_instance(self, self.instance, construct=True)
        else:
            self.save()
                
        c = cart_from_session(request)
        pay_type = self.cleaned_data['pago']
        
        order = order_from_cart(c, contact, pay_type, form)
        return order    


    def clean_ship_pc(self):
        data = self.cleaned_data.get('ship_pc')
        # as done in satchmo, emiting a postal code
        responses = signals.clean_postal_code.send(sender=CheckoutForm, postal=data)
        for responder, response in responses:
            if response:
                return response
        return data

    def clean(self):
        data = self.cleaned_data
        responses = signals.clean_checkout_form.send(sender=CheckoutForm, data=data)
        for responder, response in responses:
            if response:
                return response
        return data
        
























