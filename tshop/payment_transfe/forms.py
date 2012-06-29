#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
from django import forms


class TransferenciaForm(forms.Form):
    order = forms.CharField(widget=forms.HiddenInput)