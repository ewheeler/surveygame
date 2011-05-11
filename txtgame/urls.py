#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

import os

from django.conf.urls.defaults import *
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    # serve assets via django, during development
    #url(r'^assets/js/(?P<path>.*)$', "django.views.static.serve",
    #{"document_root": os.path.dirname(__file__) + "/static/javascripts"}),
    #url(r'^assets/css/(?P<path>.*)$', "django.views.static.serve",
    #{"document_root": os.path.dirname(__file__) + "/static/stylesheets"}),
    #url(r'^assets/images/(?P<path>.*)$', "django.views.static.serve",
    #{"document_root": os.path.dirname(__file__) + "/static/images"}),
    #url(r'^assets/icons/(?P<path>.*)$', "django.views.static.serve",
    #{"document_root": os.path.dirname(__file__) + "/static/icons"}),
    url(r'^$', views.index),
    url(r'^puzzle/$', views.puzzle, name='puzzle'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name':'loggedout.html'}, name="logout"),
    url(r'^answers/$', views.handle_answers, name='answers'),
    url(r'^newgame/$', views.new_game, name='newgame'),
)
