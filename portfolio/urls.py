from django.conf.urls import url
from . import views

app_name = "portfolio"
urlpatterns = [
    url(r'^$',                                     views.main,    name='main'),
    url(r'^contact/?$',                            views.contact, name='contact'),
    url(r'^labs/?$',                               views.labs,    name='labs'),
    url(r'^work/(?P<work_slug>[-a-zA-Z0-9_]+)/?$', views.work,    name='work'),
    url(r'^(?P<cat_slug>[-a-zA-Z0-9_]+)/?$',       views.main,    name='main'),
]
