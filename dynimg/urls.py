#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns("namegen.views",
    url(r'^$',                     views.main),    # Start, end
    url(r'^about/$',               views.about),   # Start, "about/", end
    url(r'^contact/$',             views.contact), # Start, "contact/", end
    url(r'i/(?P<id_img>[0-9]+)/$', views.getimg),  # Start, "i/", one ore more digits (id_img), "/", end
)
