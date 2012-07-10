#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, \
    AppIndexDashboard
from admin_tools.utils import get_admin_site_name
from order.models import Order




class StatsOrdersDashboard(modules.DashboardModule):
    title = _(u'Últimos 30 días ')
    template = 'stats_order_dashboard.html'

    def is_empty(self):
        return False


