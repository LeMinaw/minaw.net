from django.contrib.admin import ModelAdmin, site

from quotes.models import Quote


class QuoteAdmin(ModelAdmin):
    def short_text(self, quote):
        if len(quote.text) > 60:
            return quote.text[:60] + "[...]"
        else:
            return quote.text

    list_display = ("__str__", "author", "year", "short_text")
    date_hierarchy = "added"
    ordering = ("added",)
    search_fields = ("text", "author")


site.register(Quote, QuoteAdmin)
