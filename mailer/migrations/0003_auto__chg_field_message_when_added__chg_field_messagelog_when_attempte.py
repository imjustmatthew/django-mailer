# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Message.when_added'
        db.alter_column('mailer_message', 'when_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'MessageLog.when_attempted'
        db.alter_column('mailer_messagelog', 'when_attempted', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'MessageLog.when_added'
        db.alter_column('mailer_messagelog', 'when_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'DontSendEntry.when_added'
        db.alter_column('mailer_dontsendentry', 'when_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'Message.when_added'
        db.alter_column('mailer_message', 'when_added', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'MessageLog.when_attempted'
        db.alter_column('mailer_messagelog', 'when_attempted', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'MessageLog.when_added'
        db.alter_column('mailer_messagelog', 'when_added', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'DontSendEntry.when_added'
        db.alter_column('mailer_dontsendentry', 'when_added', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        'mailer.dontsendentry': {
            'Meta': {'object_name': 'DontSendEntry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'mailer.message': {
            'Meta': {'object_name': 'Message'},
            'connection_kwargs_data': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_data': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '1'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'mailer.messagelog': {
            'Meta': {'object_name': 'MessageLog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_message': ('django.db.models.fields.TextField', [], {}),
            'message_data': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'when_attempted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mailer']