#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = "perso"
urlpatterns = [
    url(r'^$',                                       views.main,        name='main'),
    url(r'^publication/(?P<slug>[-a-zA-Z0-9_]+)/?$', views.publication, name='publication'),
    url(r'^tag/(?P<slug>[-a-zA-Z0-9_]+)/?$',         views.tag,         name='tag'),
    url(r'^category/(?P<slug>[-a-zA-Z0-9_]+)/?$',    views.category,    name='category'),
]
