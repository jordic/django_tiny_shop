#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::
    ADMIN_TOOLS_MENU = 'gshop.menu.CustomMenu'
"""

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu
import signals

class ShopMenu(Menu):
    """
    Custom Menu for gshop admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.MenuItem(title=_('Tienda'), 
                children=[
                    items.MenuItem(_('Pedidos'), reverse('admin:order_order_changelist')),
                    items.MenuItem(_('Clientes'), reverse('admin:client_client_changelist')),
                    items.MenuItem(_('Productos'), reverse('admin:product_product_changelist')),
                    items.MenuItem(_(u'Categorías'), reverse('admin:product_category_changelist')),
                ]
                
            ),
            
            items.AppList(
                _('Administration'),
                models=('django.contrib.*',)
            )
        ]
        signals.custom_menu.send(sender=ShopMenu, menu=self)

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(ShopMenu, self).init_with_context(context)
