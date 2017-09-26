#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = "dynimg"
urlpatterns = [
    url(r'^$',                       views.main,    name="main"),    # Start, end
    url(r'^about/?$',                views.about,   name="about"),   # Start, "about/", end
    url(r'^i/(?P<id_img>[0-9]+)/?$', views.getimg,  name="getimg"),  # Start, "i/", one ore more digits (id_img), "/", end
]
