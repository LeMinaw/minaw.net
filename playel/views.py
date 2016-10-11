#-*- coding: utf-8 -*-

from django.shortcuts import render
from playel.models    import *

def main(request):
    albumsNb = Album.objects.all().count()
    
    albumsSelected = []
    if albumsNb > 4:
        albumsSelected = Album.objects.order_by('-added')[:3]
    else:
        albumsSelected = Album.objects.all()
    displayMore = albumsNb-len(albumsSelected)
    
    return render(request, "playel/main.html", locals())


def track(request, track_id, playlist_id=None, album_id=None):
    track = Track.objects.get(slug=track_id)
    
    albums = track.album_set.all()
    genres = track.igenres()
    autors = track.iautors()
    cover  = track.icover()
    covers = track.iaux_covers()
    
    return render(request, "playel/track.html", locals())

def album(request, album_id):
    album = Album.objects.get(slug=album_id)
    
    trackRels = TrackAlbumRelation.objects.filter(album=album) # Ordered by metaclass
    tracks = album.tracks.all() # Not ordered, should not be used in display template. Allows for filtering below.
    autors = album.autors.all() | Autor.objects.filter(track=tracks) # From tracks and album
    genres = album.genres.all() | Genre.objects.filter(track=tracks)
    cover  = album.cover
    covers = album.aux_covers.all()
    
    return render(request, "playel/album.html", locals())


def autor(request, autor_id):
    return render(request, "playel/playlist.html", locals())
    
    
def playlist(request, playlist_id):
    return render(request, "playel/playlist.html", locals())


def tracks(request):
    return render(request, "playel/tracks.html", locals())


def albums(request):
    albums = Album.objects.all()
    
    return render(request, "playel/albums.html", locals())


def autors(request):
    autors = Autor.objects.all()
    
    return render(request, "playel/autors.html", locals())
    
    
def playlists(request):
    return render(request, "playel/playlists.html", locals())


def about(request):
    return render(request, "playel/about.html", locals())
