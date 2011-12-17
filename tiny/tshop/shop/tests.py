"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from cart import Cart
from django.test.client import RequestFactory
from django.conf import settings

class SimpleTest(TestCase):
   
    def setUp(self):
        # Every test needs a client.
        self.req = RequestFactory()
   
   
    def test_cart_test(self):
        c = Cart()
        c.add((1,1,1))
        self.assertEqual(c[0][0], 1)
        c.append((2,2,2))
        self.assertEqual(c[1][0], 2)
        self.assertEqual(c.total(), 2)
        self.assertEqual(c.total_items(), 3)
        c.delete(0)
        self.assertEqual(c.total(), 1)
        self.assertEqual(c[0][0], 2)
        self.assertEqual(c.total_items(), 2)
        
        
        

    #def test_save_to_session(self):
        #c = Cart((1,1,1))
        #c.save(self.req)
        
        #print self.req.session[settings.CART_SESSSION_NAME]