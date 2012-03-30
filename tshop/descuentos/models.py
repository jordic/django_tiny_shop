#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ^ la línia superior serveix per poder posar accents a l'arxiu
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
""" 

"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Descuento(models.Model):
    codigo = models.CharField(blank=False, max_length=100)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Descuento en porcentaje"))
    activo = models.BooleanField(default=True)
    
    def __unicode__(self):
        return u"Código %s - %s%%" % ( self.codigo, self.descuento )


