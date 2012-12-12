#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django.contrib import admin
from models import *


class ShopCountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'active')
    list_editable = ('active',)



admin.site.register(ShopCountry, ShopCountryAdmin)
