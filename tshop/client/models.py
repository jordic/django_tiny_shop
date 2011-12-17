#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
Tiny Client model
'''


from django.db import models
from django.contrib.localflavor.es.es_provinces import PROVINCE_CHOICES

# Create your models here.

class Client(models.Model):
    
    full_name = models.CharField(blank=False, max_length=255, verbose_name=u"Nombre Completo")
    email = models.EmailField(blank=False, max_length=150, verbose_name=u"Email")
    phone = models.CharField(blank=False, max_length=80, verbose_name=u"Teléfono de Contacto")
    
    # shipping address
    ship_address = models.CharField(blank=False, max_length=255, verbose_name=u"Dirección de Envío")
    ship_pc = models.CharField(blank=False, max_length=80, verbose_name=u"Código Postal")
    ship_provincia = models.CharField(blank=False, verbose_name="Provincia", choices=PROVINCE_CHOICES, 
        max_length=50)
    ship_city = models.CharField(blank=False, max_length=255, verbose_name=u"Ciudad")
    ship_text = models.TextField(blank=True, verbose_name=u"Comentarios")
        
    lopd = models.BooleanField(default=True, verbose_name=u"Acepta LOPD?")

    def __unicode__(self):
        return "%s <%s>" % (self.full_name, self.email)