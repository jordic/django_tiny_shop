#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django import template
from django.db import models
from product.models import Product, Category
from stocks.models import Stock
from templatetag_sugar.register import tag
from templatetag_sugar.parser import Name, Variable, Constant, Optional, Model
from django.core.cache import cache
from django.utils.translation import get_language

register = template.Library()


@tag(register, [Variable(), Constant('as'), Name()])
def get_stock(context, stock, asvar):
    
    products = Product.objects.all()
    prod = {}
    st = stock.get_product_stocks()

    for p in products:
        qty = st.get(p.pk, 0)
        prod[p.pk] = (p, qty)
        


    context[asvar] = {
        'stocks'    : st,
        'products'  : prod
    }
    return ''

    #request.cart = val
    #return None