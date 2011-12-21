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
from countries import COUNTRIES

def on_create_form(sender, form, **kwargs):
    #print "Form create %s" % type(form)
    form.fields.insert( 3, 'country', forms.ChoiceField(choices=COUNTRIES) )

signals.checkout_form_created.connect(on_create_form)

# testing a validation signal on Postal Code Canarias
def validate_cp(sender, postal, **kwargs):
    CODIS_CANARIES = ['35', '38']
    print "Postal coded introduced: %s" % postal
    if postal[0:2] in CODIS_CANARIES:
        raise forms.ValidationError(u"Lo sentimos, pero no realizamos envíos a las Canarias")
    return postal

signals.clean_postal_code.connect(validate_cp)


def extra_form_validation(sender, data, **kwargs):
    if data['ship_provincia'] != data['ship_pc'][0:2]:
        raise forms.ValidationError(u"El código postal y la provincia no coinciden")

signals.clean_checkout_form.connect(extra_form_validation)