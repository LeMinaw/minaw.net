#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = "namegen"
urlpatterns = [
    url(r'^$',        views.main,  name="main"),  # Start, end
    url(r'^about/?$', views.about, name="about"), # Start, "about/", end
    url(r'^top/?$',   views.top,   name="top"),   # Start, "top/", end
    url(r'^l/$',      views.like,  name="like"),  # Start, "l/", end
]
