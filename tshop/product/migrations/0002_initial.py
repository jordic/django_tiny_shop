# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('product_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_es', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_fr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug_es', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('slug_en', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('slug_fr', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('slug_it', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('slug_de', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('text_es', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_it', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('product', ['Category'])

        # Adding model 'Product'
        db.create_table('product_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.Category'])),
            ('title_es', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_fr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug_es', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('slug_en', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('slug_fr', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('slug_it', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('slug_de', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('text_es', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_it', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=6, decimal_places=2, blank=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('subtitulo_es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('subtitulo_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('subtitulo_fr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('subtitulo_it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('subtitulo_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('resumen_es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('resumen_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('resumen_fr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('resumen_it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('resumen_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('product', ['Product'])

        # Adding model 'Options'
        db.create_table('product_options', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='variations', to=orm['product.Product'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('product', ['Options'])

        # Adding model 'Price'
        db.create_table('product_price', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='prices', to=orm['product.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal('product', ['Price'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('product_category')

        # Deleting model 'Product'
        db.delete_table('product_product')

        # Deleting model 'Options'
        db.delete_table('product_options')

        # Deleting model 'Price'
        db.delete_table('product_price')


    models = {
        'product.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug_de': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_es': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_it': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'text_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_es': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'product.options': {
            'Meta': {'object_name': 'Options'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'variations'", 'to': "orm['product.Product']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'product.price': {
            'Meta': {'object_name': 'Price'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prices'", 'to': "orm['product.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'product.product': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.Category']"}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'resumen_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'resumen_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'resumen_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'resumen_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'resumen_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug_de': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_es': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_it': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subtitulo_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subtitulo_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subtitulo_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subtitulo_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subtitulo_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'text_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_es': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['product']