from django.contrib import admin
from portfolio.models import Work, Category


admin.site.site_title = "Admin minaw.net"
admin.site.site_header = "Administration des services minaw.net"
admin.site.index_title = "Index de l'administration"


class WorkAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'pin', 'bck', 'slug', 'added')
    list_filter         = ('categ', 'pin', 'bck')
    date_hierarchy      = 'added'
    ordering            = ('slug', 'title')
    search_fields       = ('title', 'subtitle', 'content')

    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'id', 'slug')
    ordering            = ('id',)
    search_fields       = ('name',)

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Work,     WorkAdmin)
admin.site.register(Category, CategoryAdmin)
