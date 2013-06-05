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
from django.db.models.signals import post_save
from order.views import email_notification
import random
import base64
from shop import signals
from django.utils.translation import ugettext_lazy as _
from manager import StatsManager

# Create your models here.
class Order(models.Model):
    
    PENDING = 'pendiente'
    PAYED = 'pagado'
    SENDED = 'enviado'
    
    STATUS_OPTIONS = (
        (PENDING, _(u'Pendiente de Pago')),
        (PAYED, _(u'Pendiente de Envío')),
        (SENDED, _(u'Enviado')),
    )
    uid = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, verbose_name=_(u"Cliente"))
    status = models.CharField(blank=True, max_length=80, choices=STATUS_OPTIONS)
    pay_type = models.CharField(blank=True, max_length=80, verbose_name=_(u"Tipo de Pago"))
    pay_date = models.DateTimeField(blank=True, null=True, verbose_name=_(u"Fecha Pago"))
    pay_total = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name=_(u"Pagado"))
    pay_id = models.CharField(blank=True, null=True, verbose_name=_(u"ID Transaccion"), max_length=255)
    pay_details = models.CharField(blank=True, max_length=255)
    send_date = models.DateTimeField(blank=True, null=True, verbose_name=_(u'Fecha envio'))
    send_type = models.CharField(max_length=250, blank=True, null=True)
    send_ref = models.CharField("Referencia Envio", max_length=250, blank=True, null=True)


    objects = models.Manager()
    stats = StatsManager()

    class Meta:
        verbose_name = _("Pedido")
        verbose_name_plural = _("Pedidos")

    def total(self):
        return self.line_set.aggregate(Sum('total'))['total__sum']

    def quantity(self):
        return self.line_set.filter(types='product').aggregate(Sum('quantity'))['quantity__sum']

    def total_no_ship(self):
        return self.line_set.exclude(types='ship').aggregate(Sum('total'))['total__sum']
        
    def shipping(self):
        return self.total() - self.total_no_ship()
        
    def line_ordered(self):
        i = []
        for a in self.line_set.all():
            i.append(a)
        
        def comp(a,b):
            if a.types == 'product' and b.types == 'ship':
                return -1
            if a.types == 'ship' and b.types == 'product':
                return 1
            
            #if b.types == 'product':
            #    return b
            return 0
        #print i
        return sorted(i, cmp=comp)

    def export(self):
        arr = []
        for k in ('uid', 'date', 'client', 'status'):
            arr.append( getattr(self, k) )
        for k in ('total', 'total_no_ship', 'shipping', 'quantity'):
            v = getattr(self, k)
            arr.append( v() )
        for k in self.client._meta.fields:
            if k.name != "id":
                arr.append( getattr(self.client, k.name) )
        ## get line export
        for k in self.line_set.filter(types=Line.PRODUCT):
            if k.product_option:
                prod = k.product_option.__unicode__()
            else:
                prod = k.product
            t = [k.quantity, prod, k.total]
            arr = arr + t
        
        return arr



    @classmethod    
    def get_export_fields(cl):
        ff =  ['uid', 'Fecha', 'Cliente', 'Status',
            'Total', 'Total s/p', u'Envío', 'Qty']
        kk = []
        ll = [  'Q1', 'P1', 'T1',
                'Q2', 'P2', 'T2',
                'Q3', 'P3', 'T3',
                'Q4', 'P4', 'T4',
                'Q5', 'P5', 'T5',
                'Q6', 'P6', 'T6',
        ]
        from client.models import Client
        from django.utils.translation import ugettext_lazy as _
        for f in Client._meta.fields:
            if f.name != "id":
                kk.append( f.name )
        return ff + kk + ll




def set_uid(sender, **kwargs):
    """ setejem el uid si es un pedido que arriba des de l'admin """
    obj = kwargs['instance']
    if not obj.uid:
        obj.uid = obj.pk
        obj.save()

post_save.connect(set_uid, sender=Order)


def generate_order_id():
    return base64.standard_b64encode(str(random.random()*1000).replace(".", ""))

def order_from_cart(cart, client, payment_type, form):
    '''Creates an order from a given session cart and a client..'''
    o = Order()
    o.client = client
    o.status = Order.PENDING
    o.pay_type = payment_type
    o.save()
    #uid = generate_order_id()
    o.uid = "0000%s-%s" % (o.pk, o.client.email[0:2])
    o.save()
    l = cart_list(cart)
    for item in l:
        print item
        en = Line.objects.create(
            order           =o, 
            types           =Line.PRODUCT, 
            product         =item[0],
            product_option  =item[1],
            quantity        =item[2],
            amount          =item[3],
            amount_discount =item[4],
            total           =item[5])
    #afegim linia de calcul dels shippings...
    amount = cart_total( l )
    cp = client.ship_pc
    signals.order_created.send(Order, order=o, client=client, amount=amount, cart=cart, form=form)
    return o
    

def confirm_payment(sender, **kwargs):
    
    try:
        order = Order.objects.get(uid=sender.invoice)
    except:
        return
    #order = Order.objects.get(uid=sender.invoice)
    order.status = Order.PAYED
    order.pay_date = sender.payment_date
    order.pay_total = sender.auth_amount
    order.pay_id = sender.txn_id
    order.save()
    email_notification(order)
    
# paypal ipn signal
payment_was_successful.connect(confirm_payment)


    
    
class Line(models.Model):
    PRODUCT = 'product'
    SHIP = 'ship'
    TAX = 'tax'
    DESCUENTO = 'descuento'
    OLD = 'old'
        
    LINE_TYPES = (
        (PRODUCT, _('Producto')),
        (SHIP, _(u'Envío')),
        (DESCUENTO, _('Descuento'))
    )
    order = models.ForeignKey(Order, blank=False, verbose_name=_(u"Pedido"))
    types = models.CharField(blank=False, max_length=20, choices=LINE_TYPES, verbose_name=_(u"Tipo Linea"))
    product = models.ForeignKey(Product, null=True, blank=True, verbose_name=_(u"Producto"))
    product_option = models.ForeignKey(Options, null=True, blank=True, verbose_name=_(u"Variación de Producto"))
    quantity = models.IntegerField(blank=True, null=True, verbose_name=_(u"Cantidad"))
    amount = models.DecimalField(blank=True, null=True, 
        max_digits=8, decimal_places=2, verbose_name=_(u"Precio/Unitario"))
    amount_discount = models.DecimalField(null=True, blank=True, 
        max_digits=8, decimal_places=2, verbose_name=_(u"Precio/Descuento"))
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_(u"Total"))
    extra = models.CharField(blank=True, max_length=255, verbose_name=_(u"Extra Info"))
    
    class Meta:
        verbose_name = _(u'Línia Pedido')
        verbose_name_plural = _('Líneas')
    
    
    
    
    
    
    
    

