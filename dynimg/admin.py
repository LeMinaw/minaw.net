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
    
    def used_by(self, imageUrl):
        return imageUrl.dynamicimg_set.all().count()
    
    list_display   = ('id', 'short_url', 'dwnlTime', 'used_by', 'created', 'last_used', 'times_used')
  # list_filter    = ()
  # date_hierarchy = 'created'
    ordering       = ('id', 'times_used', 'created')
    search_fields  = ('id', 'url')

class DynamicImgAdmin(admin.ModelAdmin):
    list_display   = ('id', 'name', 'urls_nb', 'created', 'last_used', 'times_used')
  # list_filter    = ()
  # date_hierarchy = 'created'
    ordering       = ('id', 'times_used', 'created')
    search_fields  = ('id', 'name')

admin.site.register(Stat)
admin.site.register(ImageUrl, ImageUrlAdmin)
admin.site.register(DynamicImg, DynamicImgAdmin)

