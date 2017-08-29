#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = "avatar"
urlpatterns = [
    url(r'^$',                                          views.main,    name="main"),
    url(r'^about/?$',                                   views.about,   name="about"),
    url(r'^i/(?P<id_img>[0-9a-z]+)/(?P<size>[0-9]+)/?$', views.getimg,  name="getimg"),
    url(r'^i/(?P<id_img>[0-9a-z]+)/?$',                  views.getimg,  name="getimg"),
]
