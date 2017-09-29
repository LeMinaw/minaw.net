#-*- coding: utf-8 -*-

from django.contrib import admin
from profs.models   import *

class ModuleAdmin(admin.ModelAdmin):
    def short_content(self, module):
        if len(module.content) > 60:
            return module.content[:60] + '[...]'
        else:
            return module.content

    list_display   = ('__str__', 'active', 'short_content', 'added', 'modif')
    list_filter    = ('semester', 'subject', 'teacher', 'active')
    date_hierarchy = 'added'
    ordering       = ('-added',)
    search_fields  = ('content',)
    save_as = True


class SemesterAdmin(admin.ModelAdmin):
    list_display   = ('__str__', 'slug', 'name', 'short', 'added', 'modif')
  # list_filter    = ()
    date_hierarchy = 'added'
    ordering       = ('added',)
    search_fields  = ('name',)
    save_as = True


class SubjectAdmin(admin.ModelAdmin):
    list_display   = ('__str__', 'slug', 'name', 'short', 'added', 'modif')
  # list_filter    = ()
    date_hierarchy = 'added'
    ordering       = ('added',)
    search_fields  = ('name',)


class TeacherAdmin(admin.ModelAdmin):
    list_display   = ('__str__', 'slug', 'name', 'short', 'added', 'modif')
  # list_filter    = ()
    date_hierarchy = 'added'
    ordering       = ('added',)
    search_fields  = ('name',)

    class Media:
        js = ('https://code.jquery.com/jquery-2.1.1.min.js', 'profs/js/completion.js')


class CommentAdmin(admin.ModelAdmin):
    def short_content(self, module):
        if len(module.content) > 60:
            return module.content[:60] + '[...]'
        else:
            return module.content

    list_display   = ('__str__', 'validated', 'author', 'short_content', 'added', 'modif')
    list_filter    = ('module', 'validated')
    date_hierarchy = 'added'
    ordering       = ('-validated', 'added')
    search_fields  = ('name', 'content')


admin.site.register(Module, ModuleAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Comment, CommentAdmin)
