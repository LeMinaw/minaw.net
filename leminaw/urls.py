#-*- coding: utf-8 -*-

from django.conf             import settings
from django.conf.urls        import include, url
from django.conf.urls.static import static
from django.contrib          import admin
from perso.views             import create_error_view

urlpatterns = [
    url(r'^admin/',    admin.site.urls),
    url(r'^namegen/',  include("namegen.urls")),
    url(r'^dynimg/',   include("dynimg.urls")),
    url(r'^playel/',   include("playel.urls")),
    url(r'^profs/',    include("profs.urls")),
    url(r'^avatar/',   include("avatar.urls")),
    url(r'^quotes/',   include("quotes.urls")),
    url(r'^register/', include("register.urls")),
    url(r'^blog/',     include("perso.urls")),
    url(r'^',          include("portfolio.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

handler400 = create_error_view(code=400)
handler403 = create_error_view(code=403)
handler404 = create_error_view(code=404)
handler500 = create_error_view(code=500)
