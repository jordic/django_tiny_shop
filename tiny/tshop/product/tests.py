#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Product
from decimal import *
from shop.cart import Cart
from cart import cart_list, cart_weight

class ProductModel(TestCase):
    fixtures = ['product.json']
    
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_get_product_price(self):
        ''' el fem amb el producte pk=12 '''
        #product
        p = Product.objects.get(pk=12)
        self.assertEqual( p.get_price(1), p.price)
        # 2 productes, ha de retornar.. 44.9
        self.assertEqual( float(p.get_price(2)), 44.9)
        # 3 productes, ha de retornar.. 67.35
        self.assertEqual( float(p.get_price(3)), 67.35)
        self.assertEqual( float(p.get_price(4)), 79.90)
        self.assertEqual( float(p.get_price(5)), 99.875)
        self.assertEqual( float(p.get_price(8)), 149.9)
        self.assertEqual( float(p.get_price(10)), 187.375)
        
    def test_cart_list(self):
        c = Cart()
        # add to cart el producte 12, quantitat 1
        c.add((12, None, 1))
        l = cart_list(c)
        # afegeix b el producte
        self.assertEqual( 12, l[0][0].pk )
        # retorna la quantitat de forma correcta
        self.assertEqual( 1, float(l[0][2]) )
        # retorna el preu correctament
        self.assertEqual( 24.9, float(l[0][3]) )
        # probem amb dos lines amb el mateix producte, ha d'afegir descmpte per quantitat
        c.add((12, None, 1))
        l = cart_list(c)
        self.assertEqual( 24.9, float(l[0][3]) )
        self.assertEqual( 44.9/2, float(l[0][4]) )
        # testem que el total d'items de c funciona
        self.assertEqual( c.total_items(), 2 )
        
        c.add((12, None, 3))
        l = cart_list(c)
        self.assertEqual( c.total_items(), 5 )
        self.assertEqual( c.total(), 3 )
        self.assertEqual( 79.9/4, float(l[2][4]) )
        self.assertEqual( round((79.9/4)*3, 2), round(float(l[2][5]), 2) )

    def test_cart_weight(self):
        c = Cart()
        # add to cart el producte 12, quantitat 1
        c.add((12, None, 1))
        weight = cart_weight(c)
        self.assertEqual(weight, 960)
        c.add((12, None, 2))
        self.assertEqual(cart_weight(c), 960*3)
        c.add((11, None, 1))
        self.assertEqual(cart_weight(c), (960*3)+(2800))
























