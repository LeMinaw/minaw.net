#-*- coding: utf-8 -*-

from django.contrib import admin
from dynimg.models  import *

class ImageUrlAdmin(admin.ModelAdmin):
    def short_url(self, imageUrl):
        if len(imageUrl.url) > 60:
            start = imageUrl.url[0:30]
            end   = imageUrl.url[len(imageUrl.url)-30:len(imageUrl.url)]
            return  start + '[...]' + end
        else:
            return imageUrl.url
    short_url.short_description = "URL abrégée"

    def used_by(self, imageUrl):
        return imageUrl.dynamicimg_set.count()
    used_by.short_description = "Utilisations"

    list_display   = ('short_url', 'dwnlTime', 'used_by', 'created', 'last_used', 'times_used')
    date_hierarchy = 'created'
    ordering       = ('-times_used',)
    search_fields  = ('url',)

class DynamicImgAdmin(admin.ModelAdmin):
    list_display   = ('__str__', 'name', 'get_urls_nb', 'created', 'last_used', 'times_used')
    date_hierarchy = 'created'
    ordering       = ('-times_used',)
    search_fields  = ('id', 'name')

admin.site.register(ImageUrl, ImageUrlAdmin)
admin.site.register(DynamicImg, DynamicImgAdmin)
