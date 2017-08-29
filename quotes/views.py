from django.shortcuts import render
from django.http      import Http404
from quotes.models    import *
from random           import choice


def main(request, id=None):
    if id is None:
        quote = choice(Quote.objects.all())
    else:
        try:
            quote = Quote.objects.get(pk=id)
        except Quote.DoesNotExist:
            raise Http404("Citation introuvable :-(")

    return render(request, "quotes/main.html", locals())
