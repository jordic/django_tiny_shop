#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django.contrib import admin
from models import *
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from sorl.thumbnail.admin import AdminImageMixin
from fields import TempoImageWidget
from sorl.thumbnail import ImageField
from django.conf.urls.defaults import *
from django.conf import settings


def get_prepopulated_fields():
    r = {}
    for l,k in settings.LANGUAGES:
        r['slug_%s' % l] = ('title_%s' % l ,)
    return r


class PriceInline(admin.TabularInline):
    model = Price
    extra = 0

class OptionsInline(admin.TabularInline):
    model = Options
    #fields = ('title', 'image')
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = get_prepopulated_fields()
    formfield_overrides = {ImageField:{'widget':TempoImageWidget}}
    list_display = ('title', 'category', 'price')
    inlines = [PriceInline,OptionsInline]



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = get_prepopulated_fields()
    



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

