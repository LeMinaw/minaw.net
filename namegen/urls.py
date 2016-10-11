#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns("namegen.views",
    url(r'^$',       views.main),  # Start, end
    url(r'^about/$', views.about), # Start, "about/", end
    url(r'^top/$',   views.top),   # Start, "top/", end
    url(r'l/$',      views.like),  # Start, "l/", end
)
