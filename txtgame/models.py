#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from datetime import datetime
from operator import attrgetter

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Player(User):
    @property
    def get_answers_given(self):
        return self.answers_given.all()

    @property
    def get_questions_answered(self):
        return set([a.question for a in self.get_answers_given])

    @property
    def get_num_questions_answered(self):
        return len(self.get_questions_answered)

    @property
    def get_crew(self):
        crews = None
        if hasattr(self, 'crew_set'):
            crews = self.crew_set.all()
        if not crews:
            if hasattr(self, 'crews'):
                crews = self.crews.all()
        if crews:
            return crews[0]
        else:
            return None

    class Meta:
        proxy=True 

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    mobile = models.CharField(max_length=50)

class Crew(models.Model):
    initiator = models.ForeignKey(User)
    members = models.ManyToManyField(User, related_name="crews")

    @property
    def get_members(self):
        return self.members.all()

class SurveyGame(models.Model):
    crew = models.ManyToManyField(Crew)
    current_survey = models.ManyToManyField("Survey")
    current_question = models.ForeignKey("Question")
    begin = models.DateTimeField(auto_now_add=True)

    def get_crew(self):
        return self.crew.all()[0]

    @property
    def get_current_question(self):
        question = self.current_question
        if len([p for p in self.get_players if question.pk in [q.pk for q in p.get_questions_answered]]) != 4:
            return self.current_question
        else:
            current_seq = self.current_question.sequence
            next = current_seq + 1
            next_q = Question.objects.get(sequence=next)
            self.current_question = next_q
            self.save()
            return next
        

    @property
    def get_players(self):
        crew = self.get_crew()
        if crew:
            users = crew.members.all()
            return [Player.objects.get(pk=u.pk) for u in users]
        else:
            return ""

class Survey(models.Model):
    created = models.DateTimeField()

class Question(models.Model):
    sequence = models.PositiveSmallIntegerField()

    text_second_person = models.CharField(max_length=160)
    text_third_person = models.CharField(max_length=160)
    option_a = models.CharField(max_length=160)
    option_b = models.CharField(max_length=160)

class Answer(models.Model):
    subject = models.ForeignKey(User, related_name="answers_about")
    respondant = models.ForeignKey(User, related_name="answers_given")

    TWO_OPTION_ANSWER_CHOICES = (
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'IDK'),
    )
    answer = models.CharField(max_length=1, choices=TWO_OPTION_ANSWER_CHOICES)
    question = models.ForeignKey(Question)

class ReciprocalAccuracy(models.Model):
    game = models.ForeignKey(SurveyGame)
    subject = models.ForeignKey(User, related_name="reciprocal_answers_about")
    subject_accuracy = models.CharField(max_length=100)
    respondant = models.ForeignKey(User, related_name="reciprocal_answers_given")
    respondant_accuracy = models.CharField(max_length=100)
