from django.contrib import admin
from register.models   import *


class ActivationCodeAdmin(admin.ModelAdmin):
    list_display   = ('__str__', 'active', 'rank', 'modif')
    list_filter    = ('active',)
    date_hierarchy = 'modif'
    ordering       = ('-modif',)
    search_fields  = ('code',)

class MemberAdmin(admin.ModelAdmin):
    list_display   = ('__str__', 'user_rank')
    list_filter    = ('user_rank',)
    search_fields  = ('username',)

class DiscordMemberAdmin(MemberAdmin):
    list_display   = ('__str__', 'user_rank', 'user_id')


admin.site.register(ActivationCode, ActivationCodeAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(DiscordMember, DiscordMemberAdmin)
