#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''

from models import Product, Options
from django.core.cache import cache

def cart_list(cart):
    ''' Calcs product prices with a cart with duplicate products (variations..) 
        returns a list (product, variation, qty, price, price_dicount_qty, total)
    '''
    l = []
    dupli = {}
    in_cart = []
    for c in cart:
        prod = Product.objects.get(pk=c[0])
        quantity = int(c[2])
        subpr = Options.objects.get(pk=c[1]) if c[1] else None
            
        # mirem si el producte ja es a la cistella, per agrupar...
        if dupli.get(prod.pk):
            in_cart.append(prod.pk)
            dupli[prod.pk] = dupli[prod.pk]+quantity
        else:
            dupli[prod.pk] = quantity
                    
        price = prod.price
        unit = None
        if prod.has_tabbed_price():
            precio_total = prod.get_price(quantity)
            unit = precio_total/quantity
        else:
            precio_total = price*quantity
        
        l.append([prod, subpr, quantity, price, unit, precio_total])

    # revisem productes duplicats amb descompte per quanitat..    
    for p in in_cart:
        prod = Product.objects.get(pk=p)
        if not prod.has_tabbed_price():
            continue
        precio_total = prod.get_price(dupli[p])
        #print "Precio total %s %s " % (prod.pk, precio_total)
        unitario = precio_total/dupli[p]
        k = 0
        for m in l:
            if m[0].pk==p:
                m[4] = unitario
                m[5] = m[2]*unitario
                l[k] = m
            k = k+1
    
    return l        

def cart_weight(cart):
    ''' Cart weight '''
    weight = 0
    for c in cart:
        prod = Product.objects.get(pk=c[0])
        quantity = int(c[2])
        weight = weight + (quantity * prod.weight)
    return weight


def cart_total(c):
    ''' Cart total amount '''
    amount = 0
    for k in c:
        amount = amount + k[5]
    return amount


class SimpleCartMiddleware(object):
    '''
    Middleware to support a cart in request object.
    Optimized database acces using cache framework
    '''
    def process_request(self, request):
        
        from shop.cart import cart_from_session
        c = cart_from_session(request)
        if c.total() == 0:
            request.cart = None
            return
            
        val = cache.get('cart')
        if not val:
            val = {}
            val['total'] = c.total_items()
            l = cart_list(c)
            val['price'] = cart_total(l)
            cache.set('cart', val)

        val['c'] = c
        request.cart = val
        return None













