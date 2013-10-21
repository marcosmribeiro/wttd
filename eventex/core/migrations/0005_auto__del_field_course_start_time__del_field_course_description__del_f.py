# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Course.start_time'
        db.delete_column(u'core_course', 'start_time')

        # Deleting field 'Course.description'
        db.delete_column(u'core_course', 'description')

        # Deleting field 'Course.title'
        db.delete_column(u'core_course', 'title')

        # Deleting field 'Course.id'
        db.delete_column(u'core_course', u'id')

        # Adding field 'Course.talk_ptr'
        db.add_column(u'core_course', u'talk_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['core.Talk'], unique=True, primary_key=True),
                      keep_default=False)

        # Removing M2M table for field speakers on 'Course'
        db.delete_table('core_course_speakers')


    def backwards(self, orm):
        # Adding field 'Course.start_time'
        db.add_column(u'core_course', 'start_time',
                      self.gf('django.db.models.fields.TimeField')(default=None, blank=True),
                      keep_default=False)

        # Adding field 'Course.description'
        db.add_column(u'core_course', 'description',
                      self.gf('django.db.models.fields.TextField')(default=3),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Course.title'
        raise RuntimeError("Cannot reverse this migration. 'Course.title' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Course.id'
        raise RuntimeError("Cannot reverse this migration. 'Course.id' and its values cannot be restored.")
        # Deleting field 'Course.talk_ptr'
        db.delete_column(u'core_course', u'talk_ptr_id')

        # Adding M2M table for field speakers on 'Course'
        db.create_table(u'core_course_speakers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'core.course'], null=False)),
            ('speaker', models.ForeignKey(orm[u'core.speaker'], null=False))
        ))
        db.create_unique(u'core_course_speakers', ['course_id', 'speaker_id'])


    models = {
        u'core.contact': {
            'Meta': {'object_name': 'Contact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Speaker']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.course': {
            'Meta': {'object_name': 'Course', '_ormbases': [u'core.Talk']},
            'notes': ('django.db.models.fields.TextField', [], {}),
            'slots': ('django.db.models.fields.IntegerField', [], {}),
            u'talk_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Talk']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'core.talk': {
            'Meta': {'object_name': 'Talk'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Speaker']", 'symmetrical': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']