#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''

import uuid
from django.db import models
from client.models import Client
from product.models import Product, Options
from product.cart import cart_list, cart_weight, cart_total
from django.db.models import Sum
#from shipping import calc_shipping_costs, cart_arrival_day
from paypal.standard.ipn.signals import payment_was_successful
from order.views import email_notification
import random
import base64
from shop import signals

# Create your models here.
class Order(models.Model):
    
    PENDING = 'pendiente'
    PAYED = 'pagado'
    SENDED = 'enviado'
    
    STATUS_OPTIONS = (
        (PENDING, u'Pendiente de Pago'),
        (PAYED, u'Pendiente de Envío'),
        (SENDED, u'Enviado'),
    )
    uid = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, verbose_name=u"Cliente")
    status = models.CharField(blank=True, max_length=80, choices=STATUS_OPTIONS)
    pay_type = models.CharField(blank=True, max_length=80, verbose_name=u"Tipo de Pago")
    pay_date = models.DateTimeField(blank=True, null=True, verbose_name=u"Fecha Pago")
    pay_total = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name=u"Pagado")
    pay_id = models.CharField(blank=True, null=True, verbose_name=u"ID Transaccion", max_length=255)
    pay_details = models.CharField(blank=True, max_length=255)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def total(self):
        return self.line_set.aggregate(Sum('total'))['total__sum']

    def quantity(self):
        return self.line_set.aggregate(Sum('quantity'))['quantity__sum']-1

    def total_no_ship(self):
        return self.line_set.exclude(types='ship').aggregate(Sum('total'))['total__sum']

def generate_order_id():
    return base64.standard_b64encode(str(random.random()*1000).replace(".", ""))

def order_from_cart(cart, client, payment_type):
    '''Creates an order from a given session cart and a client..'''
    o = Order()
    o.client = client
    o.status = 'pendiente'
    o.pay_type = payment_type
    uid = generate_order_id()
    o.uid = uid
    o.save()
    l = cart_list(cart)
    for item in l:
        print item
        en = Line.objects.create(
            order           =o, 
            types           ="product", 
            product         =item[0],
            product_option  =item[1],
            quantity        =item[2],
            amount          =item[3],
            amount_discount =item[4],
            total           =item[5])
    #afegim linia de calcul dels shippings...
    amount = cart_total( l )
    cp = client.ship_pc
    signals.order_created.send(Order, order=o, client=client, amount=amount, cart=cart)
    #shipping_costs = calc_shipping_costs(cart, cp, amount)
    #Line.objects.create(
    #    order       = o,
    #    types       = "ship",
    #    quantity    = 1,
    #    total       = shipping_costs)
    return o
    

def confirm_payment(sender, **kwargs):
    try:
        order = Order.objects.get(uid=sender.invoice)
        order.status = 'pagado'
        order.pay_date = sender.payment_date
        order.pay_total = sender.auth_amount
        order.pay_id = sender.txn_id
        order.save()
        email_notification(order)
    except:
        pass
# paypal ipn signal
payment_was_successful.connect(confirm_payment)


    
    
class Line(models.Model):
    PRODUCT = 'product'
    SHIP = 'ship'
    TAX = 'tax'
        
    LINE_TYPES = (
        (PRODUCT, 'Producto'),
        (SHIP, u'Envío'),
    )
    order = models.ForeignKey(Order, blank=False, verbose_name=u"Pedido")
    types = models.CharField(blank=False, max_length=20, choices=LINE_TYPES, verbose_name=u"Tipo Linea")
    product = models.ForeignKey(Product, null=True, blank=True, verbose_name=u"Producto")
    product_option = models.ForeignKey(Options, null=True, blank=True, verbose_name=u"Variación de Producto")
    quantity = models.IntegerField(blank=True, null=True, verbose_name=u"Cantidad")
    amount = models.DecimalField(blank=True, null=True, 
        max_digits=8, decimal_places=2, verbose_name=u"Precio/Unitario")
    amount_discount = models.DecimalField(null=True, blank=True, 
        max_digits=8, decimal_places=2, verbose_name=u"Precio/Descuento")
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=u"Total")
    extra = models.CharField(blank=True, max_length=255, verbose_name=u"Extra Info")
    
    
    
    
    
    
    
    
    
    

