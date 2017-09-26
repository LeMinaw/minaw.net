#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = "quotes"
urlpatterns = [
    url(r'^$',                 views.main, name="main"),
    url(r'^(?P<id>[0-9]+)/?$', views.main, name="main"),
]
