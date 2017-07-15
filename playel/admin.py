#-*- coding: utf-8 -*-

from django.contrib import admin
from playel.models  import *

def shorten(field, chars=30):
    if len(field) > chars:
        start = field[0                  : chars/2   ]
        end   = field[len(field)-chars/2 : len(field)]
        return  start + '[...]' + end
    else:
        return field

class TrackAlbumRelationInline(admin.TabularInline):
    model = TrackAlbumRelation
    extra = 1


class TrackAdmin(admin.ModelAdmin):
    def sh_file_ogg(self, track):
        try:
            return shorten(track.file_ogg.path)
        except ValueError:
            return None

    def sh_file_mp3(self, track):
        try:
            return shorten(track.file_mp3.path)
        except ValueError:
            return None

    list_display   = ('name', 'slug', 'pub_date', 'duration', 'sh_file_ogg', 'sh_file_mp3', 'added', 'plays_nb')
    list_filter    = ('album', 'autors', 'genres', 'cover', 'aux_covers')
  # date_hierarchy = 'added'
    ordering       = ('slug', 'name')
    search_fields  = ('slug', 'name', 'file_ogg', 'file_mp3')

    prepopulated_fields = {'slug':('name',)}
    filter_horizontal   = ('autors', 'genres', 'aux_covers')
    inlines             = (TrackAlbumRelationInline,)


class AlbumAdmin(admin.ModelAdmin):
    def tracks_in(self, album):
        return album.track_set.all()#.count()

    list_display   = ('name', 'slug', 'tracks_in', 'pub_date', 'added')
    list_filter    = ('genres', 'autors', 'cover', 'aux_covers')
  # date_hierarchy = 'added'
    ordering       = ('slug', 'name')
    search_fields  = ('slug', 'name')

    prepopulated_fields = {'slug':('name',)}
    filter_horizontal   = ('genres', 'autors', 'aux_covers')
    inlines             = (TrackAlbumRelationInline,)


class AutorAdmin(admin.ModelAdmin):
    list_display        = ('name', 'slug', 'added', 'b_date', 'd_date')
  # list_filter         = ('genres', 'autors') # Old fields
  # date_hierarchy      = 'modified'
    ordering            = ('slug', 'name')
    search_fields       = ('slug', 'name')
    prepopulated_fields = {'slug':('name',)}

  # filter_horizontal = ('genres', 'autors') # Old fields


class GenreAdmin(admin.ModelAdmin):
    list_display        = ('name', 'slug', 'b_date', 'added')
    list_filter         = ('parent_genres',)
  # date_hierarchy      = 'modified'
    ordering            = ('slug', 'name')
    search_fields       = ('slug', 'name')
    prepopulated_fields = {'slug':('name',)}

    filter_horizontal = ('parent_genres',)


class CoverAdmin(admin.ModelAdmin):
    def img_path(self, cover):
        return shorten(cover.image.path, 60)

    list_display        = ('name', 'slug', 'img_path', 'added')
    list_filter         = ('cover_autors',)
  # date_hierarchy      = 'added'
    ordering            = ('slug', 'name')
    search_fields       = ('slug', 'name', 'image')
    prepopulated_fields = {'slug':('name',)}

    filter_horizontal = ('cover_autors',)


class CoverAutorAdmin(admin.ModelAdmin):
    list_display        = ('name', 'slug', 'b_date', 'd_date', 'added')
  # list_filter         = ()
  # date_hierarchy      = 'added'
    ordering            = ('slug', 'name')
    search_fields       = ('slug', 'name')
    prepopulated_fields = {'slug':('name',)}

  # filter_horizontal = list_filter


# admin.site.register(Track, TrackAdmin)
# admin.site.register(Album, AlbumAdmin)
# admin.site.register(Autor, AutorAdmin)
# admin.site.register(Genre, GenreAdmin)
# admin.site.register(Cover, CoverAdmin)
# admin.site.register(CoverAutor, CoverAutorAdmin)
