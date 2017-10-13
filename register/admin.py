from django.contrib import admin
from register.models   import *


class ActivationCodeAdmin(admin.ModelAdmin):
    list_display   = ('__str__', 'active', 'active_disc', 'rank', 'modif')
    list_filter    = ('active',)
    date_hierarchy = 'modif'
    ordering       = ('-modif',)
    search_fields  = ('code',)
    actions = ['make_active', 'make_disc_active']

    def make_active(self, request, queryset):
        rows_updated = queryset.update(active=True)
        self.message_user(request, "%s code(s) activé(s)" % rows_updated)
    make_active.short_description = "Activer les codes"

    def make_disc_active(self, request, queryset):
        rows_updated = queryset.update(active_disc=True)
        self.message_user(request, "%s code(s) Discord activé(s)" % rows_updated)
    make_disc_active.short_description = "Activer les codes Discord"


class MemberAdmin(admin.ModelAdmin):
    list_display   = ('__str__', 'user_rank')
    list_filter    = ('user_rank',)
    search_fields  = ('username',)


class DiscordMemberAdmin(MemberAdmin):
    list_display   = ('__str__', 'user_rank', 'user_id')


admin.site.register(ActivationCode, ActivationCodeAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(DiscordMember, DiscordMemberAdmin)
