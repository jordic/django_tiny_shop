# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SermepaResponse'
        db.create_table('sermepa_sermeparesponse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('Ds_Date', self.gf('django.db.models.fields.DateField')()),
            ('Ds_Hour', self.gf('django.db.models.fields.TimeField')()),
            ('Ds_SecurePayment', self.gf('django.db.models.fields.IntegerField')()),
            ('Ds_MerchantData', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('Ds_Card_Country', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('Ds_Card_Type', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('Ds_Terminal', self.gf('django.db.models.fields.IntegerField')()),
            ('Ds_MerchantCode', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('Ds_ConsumerLanguage', self.gf('django.db.models.fields.IntegerField')()),
            ('Ds_Response', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('Ds_Order', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('Ds_Currency', self.gf('django.db.models.fields.IntegerField')()),
            ('Ds_Amount', self.gf('django.db.models.fields.IntegerField')()),
            ('Ds_Signature', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('Ds_AuthorisationCode', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('Ds_TransactionType', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('Ds_Merchant_Identifier', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('Ds_ExpiryDate', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('Ds_Merchant_Group', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('Ds_Card_Number', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
        ))
        db.send_create_signal('sermepa', ['SermepaResponse'])


    def backwards(self, orm):
        # Deleting model 'SermepaResponse'
        db.delete_table('sermepa_sermeparesponse')


    models = {
        'sermepa.sermeparesponse': {
            'Ds_Amount': ('django.db.models.fields.IntegerField', [], {}),
            'Ds_AuthorisationCode': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'Ds_Card_Country': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Ds_Card_Number': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'Ds_Card_Type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'Ds_ConsumerLanguage': ('django.db.models.fields.IntegerField', [], {}),
            'Ds_Currency': ('django.db.models.fields.IntegerField', [], {}),
            'Ds_Date': ('django.db.models.fields.DateField', [], {}),
            'Ds_ExpiryDate': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'Ds_Hour': ('django.db.models.fields.TimeField', [], {}),
            'Ds_MerchantCode': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'Ds_MerchantData': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'Ds_Merchant_Group': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'Ds_Merchant_Identifier': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'Ds_Order': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'Ds_Response': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'Ds_SecurePayment': ('django.db.models.fields.IntegerField', [], {}),
            'Ds_Signature': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'Ds_Terminal': ('django.db.models.fields.IntegerField', [], {}),
            'Ds_TransactionType': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'Meta': {'object_name': 'SermepaResponse'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['sermepa']