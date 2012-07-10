#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django import forms


class StatsForm(forms.Form):
    start = forms.DateField(required=True)
    end = forms.DateField(required=True)


