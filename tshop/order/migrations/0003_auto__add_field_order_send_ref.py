# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.send_ref'
        db.add_column('order_order', 'send_ref',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.send_ref'
        db.delete_column('order_order', 'send_ref')


    models = {
        'client.client': {
            'Meta': {'object_name': 'Client'},
            'bill_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bill_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bill_country': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'bill_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bill_nif': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bill_pc': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'bill_state': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "'es'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'lopd': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'ship_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ship_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ship_country': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'ship_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ship_pc': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'ship_phone': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'ship_state': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'ship_surname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'order.line': {
            'Meta': {'object_name': 'Line'},
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'amount_discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'extra': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Order']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.Product']", 'null': 'True', 'blank': 'True'}),
            'product_option': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.Options']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'types': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'order.order': {
            'Meta': {'object_name': 'Order'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client.Client']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pay_details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pay_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pay_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'send_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'send_ref': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'send_type': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        'product.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug_de': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_es': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_it': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_pt': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'text_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_es': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_pt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_pt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'product.options': {
            'Meta': {'object_name': 'Options'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tienda.Opcion']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opciones'", 'to': "orm['product.Product']"}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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
            'resumen_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resumen_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resumen_es': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'resumen_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resumen_it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resumen_pt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug_de': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_es': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_it': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_pt': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subtitulo_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subtitulo_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subtitulo_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subtitulo_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subtitulo_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subtitulo_pt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'text_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_es': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_pt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_pt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usos': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'usos_mob': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        'tienda.opcion': {
            'Meta': {'object_name': 'Opcion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'None'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_pt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['order']