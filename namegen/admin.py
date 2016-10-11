#-*- coding: utf-8 -*-

from django.contrib import admin
from namegen.models import *

class WordAdmin(admin.ModelAdmin):
    list_display   = ('word', 'likes', 'date')
  # list_filter    = ()
  # date_hierarchy = 'date'
    ordering       = ('likes', 'date')
    search_fields  = ('word',)

admin.site.register(Stats)
admin.site.register(Word, WordAdmin)
