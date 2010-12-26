# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Address'
        db.create_table('addresses_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.UsState'], null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.CanadianProvince'], null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.Country'], null=True, blank=True)),
        ))
        db.send_create_signal('addresses', ['Address'])


    def backwards(self, orm):
        
        # Deleting model 'Address'
        db.delete_table('addresses_address')


    models = {
        'addresses.address': {
            'Meta': {'object_name': 'Address'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addresses.Country']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addresses.CanadianProvince']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addresses.UsState']", 'null': 'True', 'blank': 'True'})
        },
        'addresses.canadianprovince': {
            'Meta': {'ordering': "('name',)", 'object_name': 'CanadianProvince'},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'addresses.country': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'numcode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'printable_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'addresses.usstate': {
            'Meta': {'ordering': "('name',)", 'object_name': 'UsState'},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['addresses']
