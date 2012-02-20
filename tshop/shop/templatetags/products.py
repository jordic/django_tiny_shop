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
from django.core.cache import cache
from shop.cart import cart_from_session
from product.cart import cart_list, cart_total

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

@tag(register, [Constant('as'), Name()])
def get_cart(context, asvar):
    
    c = cart_from_session(context['request'])
    val = None
    if c.total() == 0:
        context[asvar] = None
        return ''
        
    val = cache.get('cart')
    if not val:
        val = {}
        val['total'] = c.total_items()
        l = cart_list(c)
        val['price'] = cart_total(l)
        cache.set('cart', val)

    val['c'] = c
    context[asvar] = val
    return ''
    #request.cart = val
    #return None


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
    
    
    
    
    