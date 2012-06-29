#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django.conf.urls.defaults import *
from django.conf import settings 
from django.views.generic.simple import direct_to_template
import views


urlpatterns = patterns('',
        #url(r'^$', views.soon, name="soon"),
        url(r'^cart/checkout/process$', views.transferencia_process, 
            name="checkout_process"),
    )
