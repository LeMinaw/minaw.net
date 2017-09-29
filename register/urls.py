from django.conf.urls import url
from . import views

app_name = "register"
urlpatterns = [
    url(r'^$',       views.main, name='main'),
    url(r'^load/?$', views.load, name='load'),
]
