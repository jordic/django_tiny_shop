#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def email_notification(order):
    subject = settings.EMAIL_NOTIFICATION_SUBJECT
    
    context = {}
    context['order'] = order
    context['server'] = settings.SITE_DOMAIN
    
    message = render_to_string('shop/email_order_confirm.html', context)
    #dests = [k['client'].email]
    dests = settings.EMAIL_NOTIFICATION_SENDERS + [order.client.email]
    msg = EmailMessage(subject, message, settings.EMAIL_FROM, dests)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    
