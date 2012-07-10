#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'gshop.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'gshop.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, \
    AppIndexDashboard
from admin_tools.utils import get_admin_site_name
from order.models import Order
import signals


class LatestOrders(modules.DashboardModule):
    title = _(u'Últimos Pedidos')
    template = 'dashboard/latest_orders.html'

    def __init__(self, *args, **kwargs):
        super(LatestOrders, self).__init__(*args, **kwargs)
        self.objects = Order.objects.all().order_by('-date')[0:10]

    def is_empty(self):
        return False

class ShopIndexDashboard(Dashboard):
    """
    Custom index dashboard for gshop.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        '''
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('Return to site'), '/'],
                [_('Change password'),
                 reverse('%s:password_change' % site_name)],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ]
        ))
        '''
        self.children.append(LatestOrders(
            _(u'Últimos Pedidos'),
            layout='inline',
            deletable=False,
            ))
        signals.dashboard_index.send(sender=ShopIndexDashboard, 
            dashboard=self)
        

    



class ShopAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for gshop.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

        signals.app_index_dashboard.send(sender=ShopAppIndexDashboard, 
            dashboard=self)

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(ShopAppIndexDashboard, self).init_with_context(context)















