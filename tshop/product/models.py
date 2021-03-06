#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django.db import models
from sorl.thumbnail import ImageField
from forms import CartForm
from django.utils.translation import ugettext_lazy as _
from transmeta import TransMeta


class Category(models.Model):
    __metaclass__ = TransMeta
    title = models.CharField(blank=False, max_length=255, verbose_name=_(u"Título"))
    slug = models.SlugField(verbose_name=_(u"URL Amigable"))
    text = models.TextField(blank=True, verbose_name=_(u"Texto"))

    class Meta:
        verbose_name = _(u'Categoría')
        verbose_name_plural = _(u'Categorias')
        translate = ('title', 'slug', 'text')
        
    def __unicode__(self):
        return self.title

class ProductManager(models.Manager):
    
    def active(self):
        return self.get_query_set().filter(active=True)
    
    def featured(self):
        return self.get_query_set().filter(featured=True)
    
    def not_featured(self, inn):
        return self.get_query_set().exclude(pk__in=[inn])
         

class Product(models.Model):
    
    __metaclass__ = TransMeta
    
    category = models.ForeignKey(Category)
    title = models.CharField(blank=False, max_length=255, verbose_name=_(u"Título"))
    slug = models.SlugField(verbose_name=_(u"URL Amigable"))
    active = models.BooleanField(default=True, verbose_name=_(u"Activo?"))
    featured = models.BooleanField(default=False, verbose_name=_(u"Destacado?"))
    text = models.TextField(blank=True, verbose_name=_(u"Texto"))
    image = ImageField(upload_to="upload/producto/", blank=True, verbose_name=_("Imágen"))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_(u"Precio"))
    size = models.CharField(blank=True, max_length=80, verbose_name=_(u"Tamaño"))
    weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_(u"Peso en Gramos"))
    sku = models.CharField("Codigo de producto", max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    objects = ProductManager()

    class Meta:
        verbose_name = _(u'Producto')
        verbose_name_plural = _(u'Productos')
        translate = ('title', 'slug', 'text')
        ordering = ['-position']
        
    def __unicode__(self):
        return self.title

    def has_variations(self):
        """ Has the model simple product variations """
        if len(self.variations.all())>0:
            return True
        return None
    
    def get_product_form(self):
        ''' Returns a form with, product options '''
        #if self.prod_form:
        #    return self.prod_form
        c = CartForm()
        c.set_instance(instance=self)
        self.prod_form = c
        return self.prod_form

    def has_tabbed_price(self):
        ''' have the model tabbed price '''
        if len(self.prices.all())>0:
            return True
        return False

    def get_price(self, qty):
        ''' Returns a unit price for quantity'''
        if not self.has_tabbed_price():
            return self.price
        vprice = None
        for item in self.prices.all():
            if item.quantity > qty:
                break
            vprice = item
        if not vprice:
            uprice = self.price
        else:
            uprice = vprice.price / vprice.quantity
        return uprice*qty
    
    def sales_price(self):
        """ Works if modules sales is activated """
        try:
            if self.sales.active:
                return self.sales.sales_price
            return None
        except:
            return None


    
class Options(models.Model):
    product = models.ForeignKey(Product, related_name="variations")
    title = models.CharField(blank=False, max_length=255, verbose_name=_("Título"))
    image = ImageField(null=True, upload_to="upload/opciones/", blank=True, verbose_name=_("Imágen"))
    price = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2, verbose_name=_("Precio"))
    text = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name=u"Opciones de Producto"
        
    def __unicode__(self):
        return u"Opción: %s" % self.title
        
    def has_image(self):
        if self.image:
            return True
        return False
        
class Price(models.Model):
    product = models.ForeignKey(Product, related_name="prices")
    quantity = models.IntegerField(blank=False, verbose_name=_("Cantidad"))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("Precio"))

    class Meta:
        verbose_name=_("Precios Escalados")
        ordering = ('quantity',)




    