from django.contrib import admin
from quotes.models  import *


class QuoteAdmin(admin.ModelAdmin):
    def short_text(self, quote):
        if len(quote.text) > 60:
            return quote.text[:60] + '[...]'
        else:
            return quote.text

    list_display   = ('__str__', 'author', 'year', 'short_text')
    date_hierarchy = 'added'
    ordering       = ('added',)
    search_fields  = ('text', 'author')


admin.site.register(Quote, QuoteAdmin)
