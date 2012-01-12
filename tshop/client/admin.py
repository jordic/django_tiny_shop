#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
from django.contrib import admin
from models import Client

class ClientAdmin(admin.ModelAdmin):
    pass



admin.site.register(Client, ClientAdmin)