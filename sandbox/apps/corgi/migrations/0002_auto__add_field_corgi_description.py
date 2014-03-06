# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Corgi.description'
        db.add_column(u'corgi_corgi', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Corgi.description'
        db.delete_column(u'corgi_corgi', 'description')


    models = {
        u'corgi.corgi': {
            'Meta': {'object_name': 'Corgi'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'default': '5', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['corgi']