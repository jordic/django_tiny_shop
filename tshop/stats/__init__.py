#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from dashboard import StatsOrdersDashboard
from tadmin import signals

def add_to_dashboard(sender, dashboard, **kwargs):
    dashboard.children.append(StatsOrdersDashboard(
        _(u'Últimos 30 días'),
        layout='inline',
        deletable=False,
        ))

signals.dashboard_index.connect( add_to_dashboard )