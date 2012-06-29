#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''

from django.http import HttpResponseRedirect, Http404, HttpResponse, QueryDict, HttpRequest
from forms import TransferenciaForm
from order.models import Order
from order.views import email_notification
from django.core.urlresolvers import reverse

def transferencia_process(request):
    f = TransferenciaForm(request.POST)
    if f.is_valid():
        id = f.cleaned_data['order']
        o = Order.objects.get(pk=id)
        o.save()
        email_notification(o)
        return HttpResponseRedirect(reverse('return_url'))
    else:
        #cancel_url        
        return HttpResponseRedirect(reverse('cancel_url'))
