#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ^ la línia superior serveix per poder posar accents a l'arxiu
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
""" 

"""


from django.contrib import admin
from models import Descuento

class DescuentoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'activo')
    pass
    
admin.site.register(Descuento, DescuentoAdmin)


