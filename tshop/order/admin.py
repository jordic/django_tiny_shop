#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''



from django.contrib import admin
from models import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse, QueryDict, HttpRequest
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.conf.urls.defaults import *

class LineInline(admin.TabularInline):
    #readonly_fields = ('types', 'product', )
    max_num = 0
    exclude  = ('extra',)
    
    model = Line


class OrderAdmin(admin.ModelAdmin):
    inlines = [LineInline]
    list_filter = ('status',)
    list_display = ('uid', 'client', 'status', 'date', 'pay_type', 'pay_date', 'total', 'enviar')
    exclude = ('client', 'pay_details')
    readonly_fields = ('status', 'pay_date', 'date', 'pay_type', 'pay_id')
    
    def enviar(self, obj):
        if obj.status == Order.PAYED:
            return '<a href="%s">Notificar Envío</a>' % reverse('admin:notificar_comprador', args=(obj.pk,))
        else:
            return ""
    
    enviar.short_description = 'Acciones'
    enviar.allow_tags = True
    
    
    def notificar_envio(self, request, pk):
        obj = get_object_or_404(Order, pk=pk)
        subject = settings.EMAIL_SENDING_SUBJECT
        context = {}
        context['order'] = obj
        context['server'] = settings.SITE_DOMAIN
        message = render_to_string('order/email_notify_sending.html', context)
        #dests = [k['client'].email]
        dests = [obj.client.email]
        msg = EmailMessage(subject, message, settings.EMAIL_FROM, dests)
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        
        obj.status = Order.SENDED
        obj.save()
        
        messages.add_message(request, messages.SUCCESS, u"El envío ha sido notificado" )
        return HttpResponseRedirect( reverse('admin:order_order_changelist') )
        
        
    
    def get_urls(self):
        urls = super(OrderAdmin, self).get_urls()
        my_urls = patterns('',
            url(
                r'notify_buyer/(?P<pk>\d+)$',
                self.admin_site.admin_view(self.notificar_envio),
                name='notificar_comprador',
            ),
        )
        return my_urls + urls
    



admin.site.register(Order, OrderAdmin)

