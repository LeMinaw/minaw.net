from django.contrib import admin
from bikrave.models import Work, Artist


class WorkAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'pin', 'added', 'author')
    list_filter         = ('pin', 'author')
    date_hierarchy      = 'added'
    ordering            = ('added',)
    search_fields       = ('url',)


class ArtistAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'slug', 'index')
    ordering            = ('index',)
    search_fields       = ('name', 'bio', 'quote')

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Work,     WorkAdmin)
admin.site.register(Artist, ArtistAdmin)
