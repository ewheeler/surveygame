#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from .models import *

def index(req):
    crews = Crew.objects.all()
    return render_to_response("index.html",\
            {"crews":crews,\
            "tab": "dashboard"},\
            context_instance=RequestContext(req))

def puzzle(req):
    pass

@login_required
def questions(req):
    current_question = req.user.crew_set.all()[0].current_question
    crew_mates = [m for m in req.user.crew_set.all()[0].members.all() if m != req.user]
    return render_to_response("questions.html",\
            {"question":current_question,\
            "crew_mates":crew_mates,\
            "tab": "questions"},\
            context_instance=RequestContext(req))

def handle_answers(req):
    if req.method == "POST":
        print (req.POST)
        respondant = req.user
        question = Question.objects.get(pk=req.POST['question'])
        second_person_answer = req.POST['respondant']
        second_person_answer_obj = Answer.objects.create(subject=respondant,\
            respondant=respondant, answer=second_person_answer, question=question)

        third_person_answers = dict()
        for k,v in req.POST.iteritems():
            if k.startswith('subject'):
                answer = k.split('-')
                subject = User.objects.get(pk=answer[1])
                dict.update({subject:v})
                third_person_answer = Answer.objects.create(subject=subject,\
                    respondant=respondant, answer=v, question=question)
        return HttpResponseRedirect('/')
