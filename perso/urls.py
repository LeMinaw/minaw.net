#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = "perso"
urlpatterns = [
    url(r'^$',                                                  views.main,        name='main'),
    url(r'^(?P<pageId>[0-9]+)/?$',                              views.main,        name='main'),
    url(r'^about/?$',                                           views.about,       name='about'),
    url(r'^contact/?$',                                         views.contact,     name='contact'),
    url(r'^(?P<cat_slug>[-a-zA-Z0-9_]+)/?$',                    views.main,        name='main'),
    url(r'^(?P<cat_slug>[-a-zA-Z0-9_]+)/(?P<pageId>[0-9]+)/?$', views.main,        name='main'),
    url(r'^publication/(?P<slug>[-a-zA-Z0-9_]+)/?$',            views.publication, name='publication'),
    url(r'^tag/(?P<slug>[-a-zA-Z0-9_]+)/?$',                    views.tag,         name='tag'),
]
