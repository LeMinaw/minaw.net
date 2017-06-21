#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',                                                                        views.main),      # Start, end

    url(r'^about/?$',                                                                 views.about),     # Start, "about", optional "/", end

    url(r'^tracks/?$',                                                                views.tracks),    # Start, "tracks", optional "/", end
    url(r'^track/(?P<track_id>[-a-zA-Z0-9_]+)/?$',                                    views.track),     # Start, "track/", (track_id), optional "/", end

    url(r'^albums/?$',                                                                views.albums),    # Start, "albums", optional "/", end
    url(r'^album/(?P<album_id>[-a-zA-Z0-9_]+)/?$',                                    views.album),     # Start, "album/", (album_id), optional "/", end
    url(r'^album/(?P<album_id>[-a-zA-Z0-9_]+)/(?P<track_id>[-a-zA-Z0-9_]+)/?$',       views.track),     # Start, "album/", (album_id), "/", (track_id), optional "/", end

    url(r'^autors/?$',                                                                views.autors),    # Start, "autors", optional "/", end
    url(r'^autor/(?P<autor_id>[-a-zA-Z0-9_]+)/?$',                                    views.autor),     # Start, "autor/", (autor_id), optional "/", end

    url(r'^playlists/?$',                                                             views.playlists), # Start, "playlists", optional "/", end
    url(r'^playlist/(?P<playlist_id>[-a-zA-Z0-9_]+)/?$',                              views.playlist),  # Start, "playlist/", (playlist_id), optional "/", end
    url(r'^playlist/(?P<playlist_id>[-a-zA-Z0-9_]+)/(?P<track_id>[-a-zA-Z0-9_]+)/?$', views.track)      # Start, "playlist/", (playlist_id), "/" (track_id), optional "/", end
]
