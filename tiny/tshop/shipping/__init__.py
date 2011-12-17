#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
Shipping methods

'''
from product.cart import cart_weight
from django.conf import settings
from datetime import datetime, timedelta

def shipping_methods():
    return ('Correos')


def calc_shipping_costs(cart, postal, amount):
    """ Calcs shipping costs """
    # if pedidos de mas de 60€ (0 de costes de envío)
    #if amount > 60:
    #    return 0
    
    weight = cart_weight(cart)
    return correos_shipping_cost(weight)

def cart_arrival_day():
    avui = datetime.today()
    if avui.weekday() >= 4:
        entrega = next_monday()
    else:
        entrega = avui + timedelta(days=10)
    return entrega

def next_monday():
    today = datetime.today()
    return today + timedelta(days=-today.weekday(), weeks=1)


def correos_shipping_cost(we):
    if we < 100:
        return "0.8"
    elif we < 500:
        return "1.95"
    elif we < 1000:
        return "4.40"
    elif we < 2000:
        return "5.10"
    elif we < 10000:
        return "6.6"
    elif we < 20000:
        return "20"
    elif we < 25000:
        return "25"
    else:
        return "100"

