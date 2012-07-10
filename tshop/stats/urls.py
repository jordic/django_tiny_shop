#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''

from django.conf.urls.defaults import *
import views


urlpatterns = patterns('',
    url(r'^get_stats$', views.get_stats, name="stats_api"),
    url(r'^stats$', views.stats, name="stats"),
    )


