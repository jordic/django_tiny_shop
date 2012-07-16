#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
Stock module for django tiny shop

'''

from admin_tools.menu import items, Menu
from tadmin import signals as menu_signals
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from order.models import Order
from models import StockNote, Stock

from dashboard import StocksDashboard
from tadmin import signals

def add_to_dashboard(sender, dashboard, **kwargs):
    dashboard.children.append(StocksDashboard(
        _(u'Stock de productos'),
        layout='inline',
        deletable=True,
        ))

signals.dashboard_index.connect( add_to_dashboard )

# add items to menu

def add_to_menu(sender, **kwargs):
    m = kwargs.get('menu')
    m.children[1].children = m.children[1].children + [
        items.MenuItem(_('Stocks'), 
                reverse('admin:stocks_stock_changelist')),
        items.MenuItem(_('Albaranes'), 
                reverse('admin:stocks_stocknote_changelist'))
    ]


menu_signals.custom_menu.connect( add_to_menu )


# signal to create stockenote when order marked as payed..
# ............

def post_save_order(sender, **kwargs):
    inst = kwargs['instance']
    print inst
    if inst.status == Order.PAYED:
        #print inst.albaran
        if inst.albaran.count() != 0:
            # print "No te albaran..."
            note = inst.albaran.all()[0]
            note.lines.all().delete()
        else:
            stocke = Stock.objects.all()[0]
            note = StockNote()
            note.stock = stocke
            note.operation = StockNote.OPER_OUT
            note.order = inst
            note.save()
        note.add_lines_from_order( inst )

post_save.connect(post_save_order, sender=Order)



