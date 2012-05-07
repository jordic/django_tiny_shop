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
from shop import signals
from order.models import Line

###### module vars
shipping_method = None

def add_shipping_costs(sender, order, client, amount, cart, **kwargs):
    
    cost = calc_shipping_costs(cart=cart, client=client, amount=amount, postal=str(client.ship_country))
    Line.objects.create(
        order       = order,
        types       = Line.SHIP,
        quantity    = 1,
        total       = cost)   

signals.order_created.connect(add_shipping_costs)


def calc_shipping_costs(cart, postal=None, amount=None, client=None):
    """ Calcs shipping costs """
    ms = get_shipping_method()
    ship = ms(cart=cart, postal=postal, amount=amount, client=client)
    #weight = cart_weight(cart)
    return ship.calc_shipping_cost()


def register_shipping_method(c):
    global shipping_method
    shipping_method = c

def get_shipping_method():
    global shipping_method
    if not shipping_method:
        return CorreosShipping
    return shipping_method

class BaseShipping(object):
    
    def __init__(self, cart, client=None, amount=None, postal=None):
        self.cart = cart
        self.client = client
        self.amount = amount
        self.postal = postal
        
    def shipping_method(self):
        return "Default"
    
    def calc_shipping_cost(self):
        return 0
    
    def cart_arrival_day(self):
        avui = datetime.today()
        entrega = avui + timedelta(days=10)
        return entrega

        
class CorreosShipping(BaseShipping):

    def shipping_method(self):
        return "Correos Ordinario"

    def calc_shipping_cost(self):
        we = cart_weight(self.cart)
        if we < 100:
            return "0.85"
        elif we < 500:
            return "2"
        elif we < 1000:
            return "4.50"
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

def cart_arrival_day(cart=None, postal=None, amount=None, client=None):
    ms = get_shipping_method()
    ship = ms(cart=cart, postal=postal, amount=amount, client=client)
    #weight = cart_weight(cart)
    return ship.cart_arrival_day()
    

def next_monday():
    today = datetime.today()
    return today + timedelta(days=-today.weekday(), weeks=1)










