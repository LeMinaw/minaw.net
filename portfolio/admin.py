from django.contrib import admin
from .models import Work, Category


admin.site.site_title = "Admin minaw.net"
admin.site.site_header = "Administration des services minaw.net"
admin.site.index_title = "Index de l'administration"

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'pin', 'bck', 'slug', 'added')
    list_filter         = ('categ', 'pin', 'bck')
    date_hierarchy      = 'added'
    ordering            = ('slug', 'title')
    search_fields       = ('title', 'subtitle', 'content')

    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'subtitle',
                'content', 'categ', 'pin'
            )
        }),
        ("Couverture", {
            'fields': (
                'cover', 'bck', 'black_txt',
                'cover_w', 'cover_h', '_palette'
            ),
        }),
        ("Horodatage", {
            'classes': ('collapse',),
            'fields': ('added', 'modif'),
        }),
    )
    filter_horizontal = ('categ',)
    readonly_fields = (
        'cover_w', 'cover_h', '_palette',
        'added', 'modif'
    )
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display        = ('__str__', 'id', 'slug')
    ordering            = ('id',)
    search_fields       = ('name',)

    prepopulated_fields = {'slug': ('name',)}
