from django.conf.urls import url
from . import views

app_name = "bikrave"
urlpatterns = [
    url(r'^$',                                  views.main,   name='main'),
    url(r'^prod/?$',                            views.prod,   name='prod'),
    url(r'^sound/?$',                           views.sound,  name='sound'),
    url(r'^artist/(?P<slug>[-a-zA-Z0-9_]+)/?$', views.artist, name='artist'),
]
