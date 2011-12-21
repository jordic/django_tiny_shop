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
from templatetag_sugar.register import tag
from templatetag_sugar.parser import Name, Variable, Constant, Optional, Model

register = template.Library()

@register.inclusion_tag('shop/productos.html', takes_context=True)
def widget_productos(context):
    p = Product.objects.featured()[:3]
    context['productos'] = p
    return context

@tag(register, [Constant('as'), Name() ])
def get_categories(context, asvar):
    queryset = Category.objects.all()
    context[asvar] = queryset
    return ''


@register.inclusion_tag('shop/widget_category.html', takes_context=True)
def widget_category( context, category ):
    
    c = Category.objects.get(slug=category)
    # try to find showcase product
    try:
        featured = Product.objects.featured().filter(category=c)[0]
        others = Product.objects.not_featured(featured.pk).filter(category=c)
    except:
        products = Product.objects.filter(category=c, active=True)
        featured = Product.objects.filter(category=c, active=True)[0]
        others = Product.objects.filter(category=c, active=True)[1:]
    
    context['c'] = c
    context['form'] = featured.get_product_form()
    context['prod'] = featured
    context['products'] = others
    return context


@register.filter 
def multiply(value, arg): 
    return float(value) * float(arg) 
    