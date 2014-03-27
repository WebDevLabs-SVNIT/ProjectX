# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Branch'
        db.create_table(u'organisation_branch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('division', self.gf('django.db.models.fields.CharField')(default='A', max_length=1)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal(u'organisation', ['Branch'])

        # Adding model 'Subject'
        db.create_table(u'organisation_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'organisation', ['Subject'])

        # Adding model 'StudentUserProfile'
        db.create_table(u'organisation_studentuserprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='sprofile', unique=True, to=orm['auth.User'])),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organisation.Branch'])),
        ))
        db.send_create_signal(u'organisation', ['StudentUserProfile'])

        # Adding model 'FacultyUserProfile'
        db.create_table(u'organisation_facultyuserprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='tprofile', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'organisation', ['FacultyUserProfile'])

        # Adding M2M table for field subjects on 'FacultyUserProfile'
        m2m_table_name = db.shorten_name(u'organisation_facultyuserprofile_subjects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facultyuserprofile', models.ForeignKey(orm[u'organisation.facultyuserprofile'], null=False)),
            ('subject', models.ForeignKey(orm[u'organisation.subject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facultyuserprofile_id', 'subject_id'])


    def backwards(self, orm):
        # Deleting model 'Branch'
        db.delete_table(u'organisation_branch')

        # Deleting model 'Subject'
        db.delete_table(u'organisation_subject')

        # Deleting model 'StudentUserProfile'
        db.delete_table(u'organisation_studentuserprofile')

        # Deleting model 'FacultyUserProfile'
        db.delete_table(u'organisation_facultyuserprofile')

        # Removing M2M table for field subjects on 'FacultyUserProfile'
        db.delete_table(db.shorten_name(u'organisation_facultyuserprofile_subjects'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'organisation.branch': {
            'Meta': {'object_name': 'Branch'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'division': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'organisation.facultyuserprofile': {
            'Meta': {'object_name': 'FacultyUserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Faculties'", 'symmetrical': 'False', 'to': u"orm['organisation.Subject']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'tprofile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'organisation.studentuserprofile': {
            'Meta': {'object_name': 'StudentUserProfile'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organisation.Branch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'sprofile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'organisation.subject': {
            'Meta': {'object_name': 'Subject'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['organisation']