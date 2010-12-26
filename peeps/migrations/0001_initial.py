# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    depends_on = (
        ('addresses', "0002_auto__add_address"),
    )

    def forwards(self, orm):
        
        # Adding model 'Peep'
        db.create_table('peeps_peep', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=250)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('uploader', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.PeepProfile'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('hash', self.gf('django.db.models.fields.CharField')(default='be007bf0a7320bdf3f156b217049d73d3cc654d93b946eae8081a741', max_length=64)),
        ))
        db.send_create_signal('peeps', ['Peep'])


    def backwards(self, orm):
        
        # Deleting model 'Peep'
        db.delete_table('peeps_peep')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'peeps.peep': {
            'Meta': {'object_name': 'Peep'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hash': ('django.db.models.fields.CharField', [], {'default': "'c7b9b613cc58a395c070bd7031de7a4adf5032112e264720473eef57'", 'max_length': '64'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '250'}),
            'uploader': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.PeepProfile']", 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'profiles.peepprofile': {
            'Meta': {'object_name': 'PeepProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['peeps']
