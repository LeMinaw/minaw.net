#-*- coding: utf-8 -*-

from django.conf             import settings
from django.conf.urls        import include, url
from django.conf.urls.static import static
from django.contrib          import admin

urlpatterns = [
    url(r'^admin/?',   admin.site.urls),
    url(r'^tinymce/?', include('tinymce.urls')),
    url(r'^namegen/?', include("namegen.urls")),
    url(r'^dynimg/?',  include("dynimg.urls")),
    url(r'^playel/?',  include("playel.urls")),
    url(r'^profs/?',   include("profs.urls")),
    url(r'^avatar/?',  include("avatar.urls")),
    url(r'^',         include("perso.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
