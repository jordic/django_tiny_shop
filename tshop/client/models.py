#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
Tiny Client model
'''

import warnings
from django.db import models
from django.contrib.localflavor.es.es_provinces import PROVINCE_CHOICES
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.importlib import import_module

COUNTRIES = getattr(settings, 'COUNTRIES', (''))
DEFAULT_COUNTRY = getattr(settings, 'DEFAULT_COUNTRY', ('es'))

try:
    from settings import CLIENT_BASE_MODEL
except:
    CLIENT_BASE_MODEL = None


class ClientAbstractClass(models.Model):
    
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
        abstract = True



def get_base_model():
    if not CLIENT_BASE_MODEL:
        return ClientAbstractClass

    dot = CLIENT_BASE_MODEL.rindex('.')
    module_name = CLIENT_BASE_MODEL[:dot]
    class_name = CLIENT_BASE_MODEL[dot + 1:]
    try:
        _class = getattr(import_module(module_name), class_name)
        return _class
    except (ImportError, AttributeError):
        warnings.warn('%s cannot be imported' % CLIENT_BASE_MODEL,
                      RuntimeWarning)
    return ClientAbstractClass



class Client(get_base_model()):
    """ Final client model """





