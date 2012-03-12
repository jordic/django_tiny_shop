#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
    url(r'^checkout/paypal/ipn', include('paypal.standard.ipn.urls')),
    url(r'', include('shop.urls')),
    url(r'^admin/', include(admin.site.urls)),

    
)


if settings.DEBUG:
	urlpatterns += patterns('',
       (r'^media/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './media/admin/'}),
       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
    )