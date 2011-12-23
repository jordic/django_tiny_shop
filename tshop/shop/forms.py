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
from shop.cart import Cart, cart_from_session
from order.models import order_from_cart, Order
from django.shortcuts import get_object_or_404    
from django.contrib.localflavor.es.forms import *

class CheckoutForm(forms.ModelForm):
    
    pago = forms.ChoiceField(widget=RadioSelect(), 
        choices=settings.PAYMENT_MODES, initial=settings.PAYMENT_MODES_DEFAULT )
    
    
    class Meta:
        model = Client
    
    def create_order(self, request):
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
        except:
            contact = None;
    
                
        self.contact = self.save()
        c = cart_from_session(request)
        pay_type = self.cleaned_data['pago']
        
        order = order_from_cart(c, self.contact, pay_type)
        return order
        
        
    


