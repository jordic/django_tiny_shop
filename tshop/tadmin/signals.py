#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
Signals for dashboard and menu
'''

from django.dispatch import Signal


# dashboard index
dashboard_index = Signal(providing_args=['dashboard'])

# custom app Index Dashboard
app_index_dashboard = Signal(providing_args=['dashboard'])

# custom menu
custom_menu = Signal(providing_args=['menu'])



