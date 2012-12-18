#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''

from django.db import models
from transmeta import TransMeta
from django.utils.translation import ugettext_lazy as _
from shop import signals


class ShopCountry(models.Model):
    
    __metaclass__ = TransMeta

    code = models.CharField(_(u'código'), blank=None, null=True, max_length=10)
    name = models.CharField(_(u'País'), blank=True, null=True, max_length=255)
    active = models.BooleanField(_("Activa"), default=True)

    class Meta:
        translate = ('name',)
        verbose_name = u'País con tienda'
        verbose_name_plural = u'Países con tienda'
        ordering = ('code', 'name_es')


    def __unicode__(self):
        return "%s" % self.name





def get_country_list():
    obj = ShopCountry.objects.filter(active=True)
    l =  [ (k.code, k.name) for k in obj ]
    l = sorted(l, key=lambda tup: tup[1])
    return [('', _(u'Escoge país'))] + l











