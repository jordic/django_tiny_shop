#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect, Http404, HttpResponse, QueryDict, HttpRequest
from datetime import datetime, timedelta
from django.conf import settings
from django.core.urlresolvers import reverse

from product.forms import CartForm
from product.models import Product
from product.cart import cart_list, cart_total
from shop.cart import Cart, cart_from_session
from shop.forms import CheckoutForm
from shipping import calc_shipping_costs, cart_arrival_day
from order.models import Order
from payment import get_payment
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.utils.translation import get_language
import signals
# Create your views here.

DISABLE_PRODUCTS_INACTIVE = getattr(settings, "DISABLE_PRODUCTS_INACTIVE", None)



def soon(request):
    return HttpResponse("Soon")

def home(request):
    context = {}
    return direct_to_template( request, 
            template="pages/home.html",
            extra_context=context)            

@csrf_exempt            
def add_to_cart(request):
    ''' add a product to cart, with product variations if have... '''
    f = CartForm(request.POST)
    if f.is_valid():
        product = f.get_product()
        c = cart_from_session(request)
        variation = f.cleaned_data['sub'] if product.has_variations() else None
        c.add((product.pk, variation, f.cleaned_data['qty']))
        c.save(request)
    else:
        raise Http404
    
    if request.is_ajax():
        return HttpResponse('ok')
        
    return HttpResponseRedirect(reverse('view_cart'))

    
def view_cart(request):
    ''' show cart content, pass 1 from checkout '''
    c = cart_from_session(request)
    context = {}
    context['cart'] = cart_list(c) 
    context['total'] = cart_total( context['cart'] )
    return direct_to_template(request, template="shop/cart.html", extra_context=context)
    
    
def remove_from_cart(request, id):
    ''' delete an item from cart '''
    c = cart_from_session(request)
    c.delete(int(id))
    c.save(request)
    return HttpResponseRedirect(reverse('view_cart'))
    

def product_view(request, slug):
    lang = get_language()
    ''' prodcut document '''
    kw = {}
    kw[str('slug_%s' % lang)] = slug
    p = get_object_or_404(Product, **kw)
    if p.active == False and DISABLE_PRODUCTS_INACTIVE:
        raise Http404

    related = Product.objects.filter(category=p.category, active=True).exclude(pk__in=[p.pk])
    context = { 
        'product': p, 
        'form':p.get_product_form(), 
        'related':related,
        }
    return direct_to_template(request, template="shop/product.html", extra_context=context)


def checkout(request):
    f = CheckoutForm()
    c = {}
    cart = cart_from_session(request)
    #c['cart'] = cart
    #print cart.total()
    if cart.total() == 0:
        return HttpResponseRedirect(reverse('view_cart'))
    
    c['cart'] = cart_list(cart)
    c['total'] = cart_total( c['cart'] )

    if request.method == "GET":
        if request.session.get(settings.ORDER_KEY):
            uid = request.session.get(settings.ORDER_KEY)
            try:
                order = get_object_or_404(Order, uid=uid)
                f = CheckoutForm(instance=order.client)
            except:
                pass
        c['form'] = f
        return direct_to_template(request, 
            template="shop/checkout.html", 
            extra_context=c)
    if request.method == "POST":
        f = CheckoutForm(data=request.POST)
        if f.is_valid():
            order = f.create_order(request, f)
            order.client.lang = get_language()
            order.client.save()
            request.session[settings.ORDER_KEY] = order.uid
            return HttpResponseRedirect(reverse('checkout_confirm'))
        else:
            print f.errors
            c['form'] = f
            return direct_to_template(request, 
                template="shop/checkout.html", extra_context=c)
    else:
        c['form'] = f
        return direct_to_template(request, 
            template="shop/checkout.html", extra_context=c)





def checkout_confirm(request):
    uid = request.session.get(settings.ORDER_KEY)
    order = get_object_or_404(Order, uid=uid)
    if order.status == 'pendiente':
        order.new_uid()
        request.session.set(settings.ORDER_KEY, order.uid)
        c = {}
        c['order'] = order
        c['payment_template'] = "shop/%s_payment_form.html" % order.pay_type
        c['order_form'] = get_payment(order)
        
        return direct_to_template(request, 
               template="shop/checkout_confirm.html", extra_context=c)

@never_cache
@csrf_exempt       
def checkout_ok(request):
    c = {}
    #print request
    
    if request.session.get(settings.ORDER_KEY):
        uid = request.session.get(settings.ORDER_KEY)
        request.session.flush()
        try:
            order = Order.objects.get(uid=uid)
            c['order'] = order
        except:
            pass
    return direct_to_template(request, 
           template="shop/checkout_ok.html", extra_context=c)

@csrf_exempt
def checkout_cancel(request):
    c = {}
    return direct_to_template(request, 
           template="shop/checkout_ko.html", extra_context=c)

    
def shipping_cost(request):
    ''' calc shipping cost for ajax request...'''
    #if not request.is_ajax():
    #    raise Http404
    
    cart = cart_from_session(request)
    cl = cart_list(cart) 
    amount = cart_total( cl )
    
    cp = request.GET.get('cp', None)
    # aquest parxe es per tenir resultats en la vista de checkout, 
    # on preguntem els costos d'enviament a un determinat pais...
    if not cp:
        cp = request.GET.get('country')
    
    if cp != "":
        from shipping import get_shipping_method
        shipping_method = get_shipping_method()
        #print shipping_method
        result = shipping_method(cart, postal=cp, amount=amount)
    else: 
        raise Http404
    
    return direct_to_template(request, "shop/shipping_costs.html", extra_context={
        'arrival_date': cart_arrival_day(),
        'ship': result
        })        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    