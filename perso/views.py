#-*- coding: utf-8 -*-

from django.core.paginator import Paginator
from django.shortcuts      import render, render_to_response
from django.template       import RequestContext
from django.http           import HttpResponse, HttpResponseRedirect, Http404
from random                import choice, sample
from math                  import ceil
from perso.forms           import *
from perso.models          import *


def nest(iterable, count):
    """Makes a list of lists of <count> elements out of an input <iterable>."""
    outLen = int(ceil(len(iterable) / count))
    return [iterable[i * count : (i+1) * count] for i in range(outLen)]

def page_contains(paginator, element):
    """Returns the first page of <paginator> containing <element>."""
    for page_nb in paginator.page_range:
        page = paginator.page(page_nb)
        if element in page.object_list:
            return page


def main(request, pageId=1, cat_slug=None):
    if cat_slug is None:
        publications = Publication.objects.filter(pin=True)
        coverImage = choice(Cover.objects.filter(pin=True))
    else:
        try:
            categ = Category.objects.get(slug=cat_slug)
        except Category.DoesNotExist:
            if request.path.endswith('/'): # It's possible that the user requested another app without the trailing slash (minaw.net/profs)
                raise Http404()
            else:
                return HttpResponseRedirect(request.get_full_path() + '/')

        publications = Publication.objects.filter(categ=categ)
        try:
            coverImage = choice(publications.exclude(cover=None).filter(cover__pin=True)).cover
        except IndexError:
            coverImage = choice(Cover.objects.filter(pin=True))

    barItems     = Category.objects.filter(menu=True)
    moreBarItems = Category.objects.filter(menu=False)

    paginator = Paginator(publications, 3)
    page = paginator.page(pageId)
    publications = page.object_list

    lastPublications = Publication.objects.all()[:5]

    catchSentence = choice([
        "Vous venez souvent ici ?",
        "Vous appréciez mon travail ?",
        "Vous aimeriez m'aider ?"]) + " " + choice([
        "Payez moi un café.",
        "Offrez moi une part de pizza froide.",
        "Remboursez l'eau de mes pâtes."])

    tags = sorted(Tag.objects.all(), key=lambda tag: tag.get_occurences())[:16]

    if Publication.objects.count() >= 4:
        randomPublications = sample(list(Publication.objects.all()), 4)
    else:
        randomPublications = Publication.objects.all()
    randomPublications = nest(randomPublications, 2)

    if "subscribe" in request.POST:
        subForm = SubscribeForm(request.POST)
        if subForm.is_valid():
            subForm.save()
    else:
        subForm = SubscribeForm()

    if "comment" in request.POST:
        comForm = CommentForm(request.POST)
        if comForm.is_valid():
            comForm.save()
    else:
        comForm = CommentForm()

    return render(request, "perso/main.html", locals())

def publication(request, slug):
    barItems     = Category.objects.filter(menu=True)
    moreBarItems = Category.objects.filter(menu=False)

    publication = Publication.objects.get(slug=slug)
    categ = publication.categ

    try:
        coverImage = choice(Publication.objects.filter(categ=categ).exclude(cover=None).filter(cover__pin=True)).cover
    except IndexError:
        coverImage = choice(Cover.objects.filter(pin=True))

    try:
        prev_pub = Publication.get_previous_by_added(publication)
    except Publication.DoesNotExist:
        prev_pub = None
    try:
        next_pub = Publication.get_next_by_added(publication)
    except Publication.DoesNotExist:
        next_pub = None

    if "comment" in request.POST:
        comForm = CommentForm(request.POST)
        if comForm.is_valid():
            comForm.save()
    else:
        comForm = CommentForm()

    return render(request, "perso/publi.html", locals())

def tag(request, slug):
    return render(request, "perso/tag.html", locals())

def about(request):
    barItems     = Category.objects.filter(menu=True)
    moreBarItems = Category.objects.filter(menu=False)

    coverImage = choice(Cover.objects.filter(pin=True))

    return render(request, "perso/about.html", locals())

def contact(request):
    barItems     = Category.objects.filter(menu=True)
    moreBarItems = Category.objects.filter(menu=False)

    coverImage = choice(Cover.objects.filter(pin=True))

    return render(request, "perso/contact.html", locals())


def create_error_view(code):
    def error_view(request, *args, **kwargs):
        barItems     = Category.objects.filter(menu=True)
        moreBarItems = Category.objects.filter(menu=False)

        coverImage = choice(Cover.objects.filter(pin=True))

        response = render(request, "perso/error.html", locals())
        response.status_code = code
        return response
    return error_view
