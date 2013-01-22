#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ^ la línia superior serveix per poder posar accents a l'arxiu
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
""" 
"""


from shop import signals
from django import forms
from django.utils.translation import ugettext as _
from models import Descuento

def on_create_form(sender, form, **kwargs):
    #print "Form create %s" % type(form)
    pos = len(form.fields) - 2
    form.fields.insert( pos, 'descuento', forms.CharField(required=False, max_length=100, label=_(u"Código de Descuento")) )

signals.checkout_form_created.connect(on_create_form)


def validate_discount(sender, data, **kwargs):
    """ Validates a discount code """
    descuento = data.get('descuento', None)
    if not descuento:
        valid = True
    else:
        valid = None
    try:
        elcodi = Descuento.objects.get(codigo=descuento)
        if elcodi.activo == True:
            valid = True
    except:
        pass
    if not valid:
        raise forms.ValidationError(_(u"El código de descuento introducido no es válido"))

#signals.clean_checkout_form.connect(validate_discount)


def add_discount_line(sender, order, client, amount, cart, form, **kwargs):
    
    if form.cleaned_data['descuento']:
        #print "Codigo de descuento %s" % form.cleaned_data['descuento'] 
        try:
            discount = Descuento.objects.get(codigo=form.cleaned_data['descuento'])
        except:
            return None
        total = -(order.total_no_ship()*discount.descuento)/100
        from order.models import Line
        Line.objects.create(
            order       = order,
            types       = Line.DESCUENTO,
            quantity    = 1,
            total       = str(total))
    
signals.order_created.connect(add_discount_line)

