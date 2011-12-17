#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''



from django.contrib import admin
from models import *

class LineInline(admin.TabularInline):
    #readonly_fields = ('types', 'product', )
    max_num = 0
    exclude  = ('extra',)
    
    model = Line


class OrderAdmin(admin.ModelAdmin):
    inlines = [LineInline]
    list_filter = ('status',)
    list_display = ('client', 'status', 'date', 'pay_type', 'pay_date', 'total')
    
    



admin.site.register(Order, OrderAdmin)

