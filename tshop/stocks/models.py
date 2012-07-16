#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''




from django.db import models
from django.utils.translation import ugettext_lazy as _
from product.models import Product
from order.models import Order
from django.db import connection


class Stock(models.Model):
    ''' es un magatzem '''
    name = models.CharField(max_length=100, verbose_name=_('Nombre'), blank=None, null=False)

    def disponibles(self, producto):
        pass

    class Meta:
        verbose_name=_('Almacen')
        verbose_name_plural = _('Alamcenes')

    def __unicode__(self):
        return self.name

    def get_product_stocks(self):
        query = '''SELECT product_id, sum(quantity) from 
                stocks_stocknoteline as a
                LEFT JOIN stocks_stocknote as b 
                ON a.stock_note_id = b.id
                WHERE b.stock_id = %s
                group by product_id '''
        cursor = connection.cursor()
        cursor.execute(query, [self.pk])
        res = cursor.fetchall()

        d = {}
        for k in res:
            d[k[0]] = k[1]

        return d
        




class StockNote(models.Model):
    ''' representa uns entrada o sortida de stock dun magatzem '''
    OPER_IN = 'entrada'
    OPER_OUT = 'salida'
    OPERATIONS = (
        (OPER_IN, _(u'Entrada')),
        (OPER_OUT, _('Salida'))
        )

    PENDING = 'pendiente'
    RECEIVED = 'recibido'

    STATUS = (
        (PENDING, _(u'Pendiente')),
        (RECEIVED, _(u'Recibido'))
        )

    stock = models.ForeignKey(Stock)
    operation = models.CharField(max_length=30, blank=False, null=True, choices=OPERATIONS)
    date = models.DateField(auto_now_add=True, blank=None, null=False)
    status = models.CharField(blank=True, null=True, choices=STATUS, max_length=20)
    date_delivery = models.DateField(blank=True, null=True, verbose_name=_('Fecha Entrega'))
    order = models.ForeignKey(Order, blank=True, null=True, related_name="albaran")


    class Meta:
        verbose_name=_('Albaran')
        verbose_name_plural = _('Albaranes')


    def add_lines_from_order(self, order):
        from order.models import Line
        for l in order.line_set.all():
            if l.types == Line.PRODUCT:
                s = StockNoteLine()
                s.product = l.product
                s.quantity = -(l.quantity)
                s.stock_note = self
                s.save()



class StockNoteLine(models.Model):
    ''' representa una linia de producte moguda '''
    stock_note = models.ForeignKey(StockNote, related_name='lines')
    product = models.ForeignKey(Product, related_name='stock', 
        verbose_name=_('Producto'))
    quantity = models.IntegerField(max_length=10, null=True, blank=False, 
        verbose_name=_('Cantidad'))
    price = models.DecimalField(max_digits=8, decimal_places=2,
        null=True, blank=True, verbose_name=_('Precio de Compra'))

    class Meta:
        verbose_name = _('Linia de Almacen')













