#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django import forms
from django.conf import settings as conf
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

PRODUCT_QTY_FORM = getattr(settings, 'PRODUCT_QTY_FORM', 10)

class CartForm(forms.Form):
    
    CHOICES = [(k,k) for k in range(1, PRODUCT_QTY_FORM)]
    
    def set_instance(self, instance):
        self.fields['pk'].initial = instance.pk
        if instance.has_variations():
            self.fields['sub'] = forms.ChoiceField(choices=self.get_variations(instance), label=_(conf.LABEL_VARIATIONS))
    
    def get_variations(self, instance):
        return [(str(op.pk), op.title) for op in instance.variations.all()]

    def get_product(self):
        from models import Product
        return Product.objects.get(pk=self.cleaned_data['pk'])

    pk = forms.IntegerField( widget=forms.HiddenInput, required=True )
    sub = forms.IntegerField( widget=forms.HiddenInput, required=False)
    qty = forms.ChoiceField(choices=CHOICES, label=_("Cantidad"), initial=1 )

    
