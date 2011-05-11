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
    game = None
    player = Player.objects.get(pk=req.user.pk)
    if player:
        crew = player.get_crew
        games = crew.surveygame_set.all()
        if games:
            game = crew.surveygame_set.all()[0]
    return render_to_response("index.html",\
            {"game":game,\
            "tab": "dashboard"},\
            context_instance=RequestContext(req))

def puzzle(req):
    pass

@login_required
def questions(req):
    player = Player.objects.get(pk=req.user.pk)
    if player:
        crew = player.get_crew
        game = None
        games = crew.surveygame_set.all()
        if games:
            game = crew.surveygame_set.all()[0]
        current_question = game.get_current_question
        if current_question in player.get_questions_answered:
            waiting_for_crew = True
        else:
            waiting_for_crew = False
        crew_mates = [m for m in crew.members.all() if m != req.user]
        return render_to_response("questions.html",\
                {"question":current_question,\
                "crew_mates":crew_mates,\
                "waiting_for_crew": waiting_for_crew,\
                "game":game,\
                "tab": "questions"},\
                context_instance=RequestContext(req))

def handle_answers(req):
    if req.method == "POST":
        player = Player.objects.get(pk=req.user.pk)
        respondant = player
        question = Question.objects.get(pk=req.POST['question'])
        game = SurveyGame.objects.get(pk=req.POST['game'])
        second_person_answer = req.POST['respondant']
        second_person_answer_obj = Answer.objects.create(subject=respondant,\
            respondant=respondant, answer=second_person_answer, question=question)

        for k,v in req.POST.iteritems():
            if k.startswith('subject'):
                answer = k.split('-')
                subject = Player.objects.get(pk=answer[1])
                third_person_answer = Answer.objects.create(subject=subject,\
                    respondant=respondant, answer=v, question=question)
                scores,created = ReciprocalAccuracy.objects.get_or_create(subject=subject, respondant=respondant, game=game)
        return render_to_response("success.html",\
            context_instance=RequestContext(req))

def new_game(req):
    if req.method == "POST":
        crew_info = dict()
        initiator_name = req.POST['initiator-name']
        initiator_mobile = req.POST['initiator-mobile']
        mates = [[None,None],[None,None],[None,None]]
        for k,v in req.POST.iteritems():
            if k.startswith('crewmate'):
                raw_list = k.split('-')
                if raw_list[2] == "name":
                    mates[int(raw_list[1])][0] = v
                else:
                    mates[int(raw_list[1])][1] = v
        init, created = User.objects.get_or_create(username=initiator_name)
        init_p, created = UserProfile.objects.get_or_create(user=init, mobile=initiator_mobile)
        
        new_crew, created = Crew.objects.get_or_create(initiator=init)
        new_crew.members.add(init)
        for mate in mates:
            m, created = User.objects.get_or_create(username=mate[0])
            m.set_password('m')
            m.save()
            p, created = UserProfile.objects.get_or_create(user=m, mobile=mate[1])
            new_crew.members.add(m)
            new_crew.save()
        new_crew.save()
        crew_mates = [m for m in new_crew.members.all() if m != init]

        new_game = SurveyGame(current_question= Question.objects.get(sequence=0))
        new_game.save()
        new_game.crew.add(new_crew)
        new_game.current_survey.add(Survey.objects.create(created=datetime.now()))
        new_game.save()

        return render_to_response("questions.html",\
            {"crew_mates":crew_mates,\
            "question":new_game.get_current_question,\
            "tab": "questions"},\
            context_instance=RequestContext(req))
