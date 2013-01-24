#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''



from django.contrib import admin
from django.db import models
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
from pyExcelerator import *
import datetime
from django.utils.translation import activate

from django.conf.urls.defaults import *

class LineInline(admin.TabularInline):
    #readonly_fields = ('types', 'product', )
    #max_num = 1
    extra = 1
    exclude  = ('extra',)
    
    model = Line


class OrderAdmin(admin.ModelAdmin):

    inlines = [LineInline]
    list_filter = ('status',)
    list_display = ('uid', 'client', 'status', 'date_c', 'pay_type', 
        'pay_date_c', 'envio', 'total', 'enviar')
    exclude = ('pay_details', 'pay_date','pay_total', 'pay_id')
    readonly_fields = ('date', 'send_date')
    date_hierarchy = 'date'
    search_fields = ['client__email', 'client__full_name', 'uid', 'client__ship_city']

    actions = ['view_orders', 'export_as_xls']
    
    def enviar(self, obj):
        if obj.status == Order.PAYED:
            return u'<a href="%s">Notificar Envío</a>' % reverse('admin:order_order_notificar_envio', args=(obj.pk,))
        else:
            return ""
    
    def pay_date_c(self, obj):
        return obj.pay_date.strftime('%d/%m/%Y')
    pay_date_c.short_description = 'Pago'
    pay_date_c.admin_order_field = 'pay_date'

    def date_c(self, obj):
        return obj.date.strftime('%d/%m/%Y')
    date_c.short_description = 'Pedido'
    date_c.admin_order_field = 'date'

    def envio(self, obj):
        return obj.send_date.strftime('%d/%m/%Y')
    envio.short_description = "Envio"    
    envio.admin_order_field = 'send_date'

    enviar.short_description = 'Acciones'
    enviar.allow_tags = True
    
    def add_view(self, request, form_url='', extra_context=None):
        self.readonly_fields = ('uid', 'send_date', )
        return super(OrderAdmin, self).add_view(request, form_url, extra_context)
    
    def change_view(self, request, form_url='', extra_context=None):
        self.readonly_fields = ('date','pay_id', 'send_date',)
        return super(OrderAdmin, self).change_view(request, form_url, extra_context)
        
    
    def view_orders(self, request, queryset):
        c = {}
        c['obj'] = queryset
        total = 0
        for k in queryset:
            total = total + k.total()
        c['total'] = total
        
        return direct_to_template(request, 'admin/order/order/view_orders.html', c)
    
    
    def notificar_envio(self, request, pk):
        #print "ara"
        obj = get_object_or_404(Order, pk=pk)
        subject = settings.EMAIL_SENDING_SUBJECT
        context = {}
        context['order'] = obj
        context['server'] = settings.SITE_DOMAIN
        activate(obj.client.lang)
        message = render_to_string('order/email_notify_sending.html', context)
        #dests = [k['client'].email]
        dests = [obj.client.email]
        msg = EmailMessage(subject, message, settings.EMAIL_FROM, dests)
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        
        obj.status = Order.SENDED
        obj.send_date = datetime.datetime.now()
        obj.save()
        
        messages.add_message(request, messages.SUCCESS, u"El envío ha sido notificado" )
        return HttpResponseRedirect( reverse('admin:order_order_changelist') )
        
        
    '''
    def get_urls(self):
        urls = super(OrderAdmin, self).get_urls()
        my_urls = patterns('',
            url(
                r'notify_buyer/(?P<pk>\d+)$',
                self.admin_site.admin_view(self.notificar_envio),
                name='notificar_comprador',
            ),
        )
        #print my_urls, urls
        return my_urls + urls
    '''
    def get_urls(self):

        from django.conf.urls.defaults import patterns, url
        info = "%s_%s" % (self.model._meta.app_label, self.model._meta.module_name)
        pat = lambda regex, fn: url(regex, self.admin_site.admin_view(fn), name='%s_%s' % (info, fn.__name__))

        url_patterns = patterns('',
            pat(r'^([0-9]+)/notify-buyer/$', self.notificar_envio),
        )

        urls = url_patterns + super(OrderAdmin, self).get_urls()
        print urls
        return urls

    
    def export_as_xls(modeladmin, request, queryset):
        """
        Generic xls export admin action.
        """
        if not request.user.is_staff:
            raise PermissionDenied

        camps = Order.get_export_fields()

        wb = Workbook()
        ws0 = wb.add_sheet('0')
        col = 0
        # write header row
        for field in camps:
            ws0.write(0, col, field)
            col = col + 1

        row = 1
        # Write data rows
        for obj in queryset:
            col = 0
            for field in obj.export():
                ws0.write(row, col, unicode(field))
                col = col + 1
            row = row + 1

        wb.save('/tmp/output.xls')
        response = HttpResponse(open('/tmp/output.xls','r').read(),
                      mimetype='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=Pedidos.xls'
        return response
    export_as_xls.short_description = "Export selected objects to XLS"




admin.site.register(Order, OrderAdmin)

