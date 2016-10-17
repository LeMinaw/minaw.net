#-*- coding: utf-8 -*-

from django.conf             import settings
from django.conf.urls        import include, url
from django.conf.urls.static import static
from django.contrib          import admin

urlpatterns = [
    url(r'^$',        include("perso.urls")),
    url(r'^admin/',   include(admin.site.urls)),
    url(r'^namegen/', include("namegen.urls")),
    url(r'^dynimg/',  include("dynimg.urls")),
    url(r'^playel/',  include("playel.urls")),
    url(r'^profs/',   include("profs.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
