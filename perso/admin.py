#-*- coding: utf-8 -*-

from django.contrib  import admin
from perso.models    import *


class PublicationAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'pin', 'slug', 'added')
    list_filter         = ('categ','tags')
    date_hierarchy      = 'added'
    ordering            = ('slug', 'title')
    search_fields       = ('title', 'subtitle', 'content')

    prepopulated_fields = {'slug':('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'id', 'slug')
    ordering            = ('id',)
    search_fields       = ('slug', 'name', 'descr')

    prepopulated_fields = {'slug':('name',)}


class TagAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'slug', 'get_occurences')
    ordering            = ('slug',)
    search_fields       = ('slug', 'name')

    prepopulated_fields = {'slug':('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'pseudo', 'email', 'added')
    list_filter         = ('publi',)
    date_hierarchy      = 'added'
    ordering            = ('pseudo', 'email')
    search_fields       = ('pseudo', 'email', 'content')


class CoverAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'pin')
    ordering            = ('name',)
    search_fields       = ('name', 'descr',)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display        = ('__str__',)
    date_hierarchy      = 'added'
    search_fields       = ('email',)


admin.site.register(Publication, PublicationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Cover, CoverAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
