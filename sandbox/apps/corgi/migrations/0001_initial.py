# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Corgi'
        db.create_table(u'corgi_corgi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=10, null=True, blank=True)),
            ('length', self.gf('django.db.models.fields.IntegerField')(default=5, null=True, blank=True)),
        ))
        db.send_create_signal(u'corgi', ['Corgi'])


    def backwards(self, orm):
        # Deleting model 'Corgi'
        db.delete_table(u'corgi_corgi')


    models = {
        u'corgi.corgi': {
            'Meta': {'object_name': 'Corgi'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'default': '5', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['corgi']