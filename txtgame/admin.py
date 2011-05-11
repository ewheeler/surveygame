#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Crew)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(SurveyGame)
admin.site.register(ReciprocalAccuracy)
