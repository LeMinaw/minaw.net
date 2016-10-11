#-*- coding: utf-8 -*-

from django.contrib import admin
from profs.models   import *

class ModuleAdmin(admin.ModelAdmin):
    def short_content(self, module):
        if len(module.content) > 60:
            return module.content[:60] + '[...]'
        else:
            return module.content
    
    list_display   = ('__unicode__', 'short_content', 'added', 'modif')
    list_filter    = ('semester', 'subject', 'teacher')
    date_hierarchy = 'added'
    ordering       = ('added',)
    search_fields  = ('content',)


class SemesterAdmin(admin.ModelAdmin):
    list_display   = ('__unicode__', 'slug', 'name', 'short', 'added', 'modif')
  # list_filter    = ()
    date_hierarchy = 'added'
    ordering       = ('added',)
    search_fields  = ('name',)


class SubjectAdmin(admin.ModelAdmin):
    list_display   = ('__unicode__', 'slug', 'name', 'short', 'added', 'modif')
  # list_filter    = ()
    date_hierarchy = 'added'
    ordering       = ('added',)
    search_fields  = ('name',)


class TeacherAdmin(admin.ModelAdmin):
    list_display   = ('__unicode__', 'slug', 'name', 'short', 'added', 'modif')
  # list_filter    = ()
    date_hierarchy = 'added'
    ordering       = ('added',)
    search_fields  = ('name',)


class CommentAdmin(admin.ModelAdmin):
    def short_content(self, module):
        if len(module.content) > 60:
            return module.content[:60] + '[...]'
        else:
            return module.content
    
    list_display   = ('__unicode__', 'validated', 'author', 'short_content', 'added', 'modif')
    list_filter    = ('module',)
    date_hierarchy = 'added'
    ordering       = ('-validated', 'added')
    search_fields  = ('name', 'content')
    
    
admin.site.register(Module, ModuleAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Comment, CommentAdmin)

