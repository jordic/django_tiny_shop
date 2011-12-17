#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------


from django.conf.urls.defaults import *
from django.conf import settings 
from django.views.generic.simple import direct_to_template
import views


urlpatterns = patterns('',
        #url(r'^$', views.soon, name="soon"),
        url(r'^$', views.home, name="home"),
        url(r'^product/(?P<slug>.*)$', views.product_view, name="product_view"),
        url(r'^cart/add$', views.add_to_cart, name="add_to_cart"),
        url(r'^cart/del/(?P<id>\d+)$', views.remove_from_cart, name="remove_from_cart"),
        url(r'^cart$', views.view_cart, name="view_cart"),
        url(r'^cart/checkout$', views.checkout, name="checkout"),
        url(r'^cart/checkout/confirm$', views.checkout_confirm, name="checkout_confirm"),
        url(r'^cart/checkout/shipping_cost$', views.shipping_cost, name="shipping_costs"),
        url(r'^cart/checkout/ok$', views.checkout_ok, name="return_url"),
        url(r'^cart/checkout/cancel$', views.checkout_cancel, name="cancel_url"),
        
    )