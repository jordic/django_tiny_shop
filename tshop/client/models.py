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
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

COUNTRIES = getattr(settings, 'COUNTRIES', (''))
DEFAULT_COUNTRY = getattr(settings, 'DEFAULT_COUNTRY', ('es'))

class Client(models.Model):
    
    full_name = models.CharField(blank=False, max_length=255, verbose_name=_(u"Nombre Completo"))
    email = models.EmailField(blank=False, max_length=150, verbose_name=_(u"Email"))
    phone = models.CharField(blank=False, max_length=80, verbose_name=_(u"Teléfono de Contacto"))
    
    # shipping address
    ship_country = models.CharField(null=True, blank=False, max_length=25, 
        verbose_name=_(u"Pais"), choices=COUNTRIES, default=DEFAULT_COUNTRY)
    ship_address = models.CharField(blank=False, max_length=255, verbose_name=_(u"Dirección de Envío"))
    ship_pc = models.CharField(blank=False, max_length=80, verbose_name=_(u"Código Postal"))
    ship_provincia = models.CharField(blank=True, verbose_name=_("Provincia"), choices=PROVINCE_CHOICES, 
        max_length=50)
    ship_city = models.CharField(blank=False, max_length=255, verbose_name=_(u"Ciudad"))
    ship_text = models.TextField(blank=True, verbose_name=_(u"Comentarios"))

        
    lopd = models.BooleanField(default=True, verbose_name=_(u"Acepta LOPD?"))
    lang = models.CharField(null=True, blank=True, max_length=10, 
        verbose_name=_(u'Idioma'))


    def __unicode__(self):
        return "%s <%s>" % (self.full_name, self.email)
        
    class Meta:
        verbose_name=_(u'cliente')
        
        
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "email__icontains", "full_name__icontains",)
        
        
        
        