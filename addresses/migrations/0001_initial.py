# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Country'
        db.create_table('addresses_country', (
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('printable_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('iso3', self.gf('django.db.models.fields.CharField')(max_length=3, null=True)),
            ('numcode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
        ))
        db.send_create_signal('addresses', ['Country'])

        # Adding model 'UsState'
        db.create_table('addresses_usstate', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('addresses', ['UsState'])

        # Adding model 'CanadianProvince'
        db.create_table('addresses_canadianprovince', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('addresses', ['CanadianProvince'])


    def backwards(self, orm):
        
        # Deleting model 'Country'
        db.delete_table('addresses_country')

        # Deleting model 'UsState'
        db.delete_table('addresses_usstate')

        # Deleting model 'CanadianProvince'
        db.delete_table('addresses_canadianprovince')


    models = {
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
