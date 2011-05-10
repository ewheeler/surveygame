#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from datetime import datetime
from operator import attrgetter

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    mobile = models.CharField(max_length=50)

class Crew(models.Model):
    initiator = models.ForeignKey(User)
    members = models.ManyToManyField(User, related_name="members")
    survey = models.ForeignKey("Survey")
    current_question = models.ForeignKey("Question")

    @property
    def get_members(self):
        return self.members.all()

class Survey(models.Model):
    begin = models.DateTimeField()

class Question(models.Model):
    survey = models.ForeignKey(Survey)
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
    question = models.ForeignKey(Question)
    subject = models.ForeignKey(User, related_name="reciprocal_answers_about")
    subject_accuracy = models.CharField(max_length=100)
    respondant = models.ForeignKey(User, related_name="reciprocal_answers_given")
    respondant_accuracy = models.CharField(max_length=100)
