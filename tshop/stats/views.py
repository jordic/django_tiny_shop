#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
from forms import StatsForm
from django.http import HttpResponseRedirect, Http404, HttpResponse, \
    QueryDict, HttpRequest
from django.views.generic.simple import direct_to_template    
from django.contrib.auth.decorators import login_required
import json
from order.models import Order
import datetime
import decimal

@login_required
def get_stats(request):
    c = StatsForm( data=request.GET )
    if c.is_valid():
        i = c.cleaned_data.get('start').strftime('%Y-%m-%d')
        e = c.cleaned_data.get('end').strftime('%Y-%m-%d')
        result = {}
        
        # total pedidios
        t = Order.stats.total(i,e)
        result['total_facturat'] = t[0][0]
        result['total_orders'] = t[0][1]

        # facturas dia
        result['facturas_dia'] = Order.stats.facturas_dia(i, e)
        # pedidos dia
        result['pedidos_dia'] = Order.stats.pedidos_dia(i, e)
        # rendiment producte
        result['rendiment_producte'] = Order.stats.rendiment_producte(i, e)
        # productes dies
        result['productes_per_dia'] = Order.stats.productes_per_dia(i, e)

        data = json.dumps( result, default=dthandler )
        res = HttpResponse( data )
        return res
    else:
        print c
        return HttpResponse('invalid_form')



# handler per la codificacio json dels tipus de camp
def dthandler(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    if isinstance(obj, decimal.Decimal):
        return float(str(obj))
    return None


@login_required
def stats(request):
    return direct_to_template(request, template="stats/stats.html")







































