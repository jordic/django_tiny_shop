#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''



from django.contrib import admin
from models import *


class StockAdmin(admin.ModelAdmin):
    pass


class StockNoteLineAdmin(admin.TabularInline):
    model = StockNoteLine
    extra = 3

class StockNoteAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'operation', 'date_delivery', 'status',)
    list_filter = ('operation',)
    exclude = ('order',)
    inlines = [StockNoteLineAdmin]



admin.site.register(Stock, StockAdmin)
admin.site.register(StockNote, StockNoteAdmin)
