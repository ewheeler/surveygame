# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'TwoOptionAnswer.id'
        db.delete_column('txtgame_twooptionanswer', 'id')

        # Adding field 'TwoOptionAnswer.answer_ptr'
        db.add_column('txtgame_twooptionanswer', 'answer_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['txtgame.Answer'], unique=True, primary_key=True), keep_default=False)

        # Deleting field 'TwoOptionQuestion.id'
        db.delete_column('txtgame_twooptionquestion', 'id')

        # Adding field 'TwoOptionQuestion.question_ptr'
        db.add_column('txtgame_twooptionquestion', 'question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['txtgame.Question'], unique=True, primary_key=True), keep_default=False)


    def backwards(self, orm):
        
        # We cannot add back in field 'TwoOptionAnswer.id'
        raise RuntimeError(
            "Cannot reverse this migration. 'TwoOptionAnswer.id' and its values cannot be restored.")

        # Deleting field 'TwoOptionAnswer.answer_ptr'
        db.delete_column('txtgame_twooptionanswer', 'answer_ptr_id')

        # We cannot add back in field 'TwoOptionQuestion.id'
        raise RuntimeError(
            "Cannot reverse this migration. 'TwoOptionQuestion.id' and its values cannot be restored.")

        # Deleting field 'TwoOptionQuestion.question_ptr'
        db.delete_column('txtgame_twooptionquestion', 'question_ptr_id')


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
            'current_question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['txtgame.Question']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['txtgame.Survey']"})
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
            'Meta': {'object_name': 'TwoOptionAnswer', '_ormbases': ['txtgame.Answer']},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'answer_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['txtgame.Answer']", 'unique': 'True', 'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['txtgame.TwoOptionQuestion']"})
        },
        'txtgame.twooptionquestion': {
            'Meta': {'object_name': 'TwoOptionQuestion', '_ormbases': ['txtgame.Question']},
            'option_a': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'option_b': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['txtgame.Question']", 'unique': 'True', 'primary_key': 'True'}),
            'text_second_person': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'text_third_person': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        'txtgame.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['txtgame']
