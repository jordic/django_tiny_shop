"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from client.models import *
from shop.cart import Cart
from order.models import order_from_cart
from product.cart import cart_list, cart_weight, cart_total
from order.models import generate_order_id
from decimal import *
from shipping import calc_shipping_costs
from order.models import Order

class SimpleTest(TestCase):
    fixtures = ['product.json']
    def test_order_from_cart(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        client = Client.objects.get(pk=1)
        self.assertEqual(client.email, 'jordic@gmail.com')
        
        c = Cart()
        c.add((12, 37, 2))
        c.add((1, None, 1))
        l = cart_list(c)
        
        order = order_from_cart(c, client, 'paypal')
        self.assertEqual(len(order.line_set.all()), 3)
        # this test fails because not shipping costs
        ship_cost = Decimal(calc_shipping_costs(c, '08695', cart_total(l)))
        self.assertEqual(order.total(), cart_total(l) + ship_cost )
        
        self.assertEqual(order.line_set.all()[2].types, 'ship' )
        self.assertEqual(order.pay_type, 'paypal' )


    def test_numeros_aleatoris(self):
        t = []
        for k in range(10000):
            num = generate_order_id()
            self.assertNotIn(num, t)
            t.append(num)
        
        #[(12L, 37, u'1')]
    
    

























