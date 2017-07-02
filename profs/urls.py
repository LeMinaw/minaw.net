#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = "profs"
urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^about/?$', views.about, name='about'),
    url(r'^contact/?$', views.contact, name='contact'),
    url(r'^modules/?$', views.modules, name='modules'),
    url(r'^module/(?P<semester>[-a-zA-Z0-9_]+)/(?P<subject>[-a-zA-Z0-9_]+)/(?P<teacher>[-a-zA-Z0-9_]+)/?$', views.module, name='module'),
]
