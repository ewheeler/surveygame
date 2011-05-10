# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('txtgame_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('txtgame', ['UserProfile'])

        # Adding model 'Crew'
        db.create_table('txtgame_crew', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('initiator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('txtgame', ['Crew'])

        # Adding M2M table for field members on 'Crew'
        db.create_table('txtgame_crew_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crew', models.ForeignKey(orm['txtgame.crew'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('txtgame_crew_members', ['crew_id', 'user_id'])

        # Adding model 'Survey'
        db.create_table('txtgame_survey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('begin', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('txtgame', ['Survey'])

        # Adding model 'Question'
        db.create_table('txtgame_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['txtgame.Survey'])),
            ('sequence', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('txtgame', ['Question'])

        # Adding model 'TwoOptionQuestion'
        db.create_table('txtgame_twooptionquestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('option_a', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('option_b', self.gf('django.db.models.fields.CharField')(max_length=160)),
        ))
        db.send_create_signal('txtgame', ['TwoOptionQuestion'])

        # Adding model 'Answer'
        db.create_table('txtgame_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers_about', to=orm['auth.User'])),
            ('respondant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers_given', to=orm['auth.User'])),
        ))
        db.send_create_signal('txtgame', ['Answer'])

        # Adding model 'TwoOptionAnswer'
        db.create_table('txtgame_twooptionanswer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['txtgame.TwoOptionQuestion'])),
        ))
        db.send_create_signal('txtgame', ['TwoOptionAnswer'])

        # Adding model 'ReciprocalAccuracy'
        db.create_table('txtgame_reciprocalaccuracy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['txtgame.Question'])),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reciprocal_answers_about', to=orm['auth.User'])),
            ('subject_accuracy', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('respondant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reciprocal_answers_given', to=orm['auth.User'])),
            ('respondant_accuracy', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('txtgame', ['ReciprocalAccuracy'])


    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('txtgame_userprofile')

        # Deleting model 'Crew'
        db.delete_table('txtgame_crew')

        # Removing M2M table for field members on 'Crew'
        db.delete_table('txtgame_crew_members')

        # Deleting model 'Survey'
        db.delete_table('txtgame_survey')

        # Deleting model 'Question'
        db.delete_table('txtgame_question')

        # Deleting model 'TwoOptionQuestion'
        db.delete_table('txtgame_twooptionquestion')

        # Deleting model 'Answer'
        db.delete_table('txtgame_answer')

        # Deleting model 'TwoOptionAnswer'
        db.delete_table('txtgame_twooptionanswer')

        # Deleting model 'ReciprocalAccuracy'
        db.delete_table('txtgame_reciprocalaccuracy')


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
        'txtgame.answer': {
            'Meta': {'object_name': 'Answer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respondant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers_given'", 'to': "orm['auth.User']"}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers_about'", 'to': "orm['auth.User']"})
        },
        'txtgame.crew': {
            'Meta': {'object_name': 'Crew'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members'", 'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'txtgame.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sequence': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['txtgame.Survey']"})
        },
        'txtgame.reciprocalaccuracy': {
            'Meta': {'object_name': 'ReciprocalAccuracy'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['txtgame.Question']"}),
            'respondant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reciprocal_answers_given'", 'to': "orm['auth.User']"}),
            'respondant_accuracy': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reciprocal_answers_about'", 'to': "orm['auth.User']"}),
            'subject_accuracy': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'txtgame.survey': {
            'Meta': {'object_name': 'Survey'},
            'begin': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'txtgame.twooptionanswer': {
            'Meta': {'object_name': 'TwoOptionAnswer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['txtgame.TwoOptionQuestion']"})
        },
        'txtgame.twooptionquestion': {
            'Meta': {'object_name': 'TwoOptionQuestion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option_a': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'option_b': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        'txtgame.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['txtgame']
