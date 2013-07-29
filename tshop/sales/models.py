#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django.db import models
from product.models import Product
from django.utils.translation import ugettext_lazy as _
from shop.signals import cart_list_created

class ProductSales(models.Model):
    product = models.OneToOneField(Product, related_name="sales")
    sales_price = models.DecimalField(max_digits=6, decimal_places=2, 
        blank=True, null=True, verbose_name=_(u"Precio Rebajado"))
    active = models.BooleanField(default=False, verbose_name=_(u"Activo?"))

    class Meta:
        verbose_name = "Rebajas"
        verbose_name_plural = "Rebajas"

    def __unicode__(self):
        return self.product.title


def on_cart_list(sender, **kwargs):
    l = kwargs['list']
    print "La cesta de la compra", l
    #[prod, subpr, quantity, price, unit, precio_total]
    new = []
    for p in l:
        product = p[0]
        if product.sales_price():
            p[4] = product.sales_price()
            p[5] = p[2] * p[4]
        new.append(p)
    l = new


cart_list_created.connect( on_cart_list )




