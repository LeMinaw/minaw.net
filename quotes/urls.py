from django.urls import path

from quotes import views

app_name = "quotes"
urlpatterns = [
    path("", views.main, name="main"),
    path("<int:id>", views.main, name="main"),
]
