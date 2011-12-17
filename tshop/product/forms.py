#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django import forms


class CartForm(forms.Form):
    
    CHOICES = [(k,k) for k in range(1,10)]
    
    def set_instance(self, instance):
        self.fields['pk'].initial = instance.pk
        if instance.has_variations():
            self.fields['sub'] = forms.ChoiceField(choices=self.get_variations(instance), label="Perfume")
    
    def get_variations(self, instance):
        return [(str(op.pk), op.title) for op in instance.variations.all()]

    def get_product(self):
        from models import Product
        return Product.objects.get(pk=self.cleaned_data['pk'])

    pk = forms.IntegerField( widget=forms.HiddenInput, required=True )
    sub = forms.IntegerField( widget=forms.HiddenInput, required=False)
    qty = forms.ChoiceField(choices=CHOICES, label="Cantidad", initial=1 )

    
