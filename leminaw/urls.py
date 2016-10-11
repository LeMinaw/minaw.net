#-*- coding: utf-8 -*-

from django.conf             import settings
from django.conf.urls        import include, url
from django.conf.urls.static import static
from django.contrib          import admin
from namegen import views
from dynimg  import views
from playel  import views
from profs   import views

urlpatterns = [
    url(r'^admin/',   include(admin.site.urls)),
    url(r'^namegen/', include("namegen.urls")),  # Start ; "namegen/" ; end
    url(r'^dynimg/',  include("dynimg.urls")),   # Start ; "dynimg/"  ; end
    url(r'^playel/',  include("playel.urls")),   # Start ; "playel/"  ; end
    url(r'profs/',    include("profs.urls")),    # Start ; "profs/"   ; end
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
