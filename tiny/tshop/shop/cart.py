#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''
from django.conf import settings
from django.core.cache import cache


class Cart(list):
    ''' Is a simple store for items, each item is represented by a tuple
        where (item.pk, option.pk, quantity)
    '''
    def add(self, item):
        self.append(item)
        
    def total(self):
        return len(self)
    
    def total_items(self):
        total = 0
        for k in self:
            total = total + int(k[2])
        return total
        
    def delete(self, p):
        del self[p]
        
    def save(self, request):
        request.session[settings.CART_SESSSION_NAME] = self
        cache.delete('cart')
    
                
    '''def get(self, request):
        return request.session[settings.CART_SESSSION_NAME]'''
        
        
def cart_from_session(request):
    if request.session.get(settings.CART_SESSSION_NAME):
        c = Cart(request.session.get(settings.CART_SESSSION_NAME))
    else:
        c = Cart()
    return c
    
    


















