#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
Método de pago por tranferencia
usado en devel para probar circuito de emails
'''



from django.conf import settings 
from django.core.urlresolvers import reverse
from django import forms
from forms import TransferenciaForm



def transferencia_form(order):
    form = TransferenciaForm(initial={'order':order.pk})
    return form









