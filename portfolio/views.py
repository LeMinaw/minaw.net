from django.shortcuts import render
from django.http      import HttpResponseRedirect, Http404
from portfolio.models import Category, Work


def main(request, cat_slug=None):
    categs = Category.objects.all()
    if cat_slug is None:
        works = Work.objects.all()
        work_cover = works.filter(bck=True).order_by('?').first()
        categ = None
    else:
        try:
            categ = Category.objects.get(slug=cat_slug)
        except Category.DoesNotExist:
            if request.path.endswith('/'):
                # It's possible that the user requested another app without the
                # trailing slash (minaw.net/profs)
                raise Http404()
            else:
                return HttpResponseRedirect(request.get_full_path() + '/')

        works = Work.objects.filter(categ=categ)
        work_cover = (works.filter(bck=True).order_by('?').first()
            or Work.objects.filter(bck=True).order_by('?').first())

    return render(request, "portfolio/main.html", locals())


def work(request, work_slug):
    categs = Category.objects.all()
    work = Work.objects.get(slug=work_slug)
    work_categs = work.categ.all()

    work_cover = (Work.objects.filter(categ__in=work_categs, bck=True).order_by('?').first()
        or Work.objects.filter(bck=True).order_by('?').first())

    try:
        prev_work = Work.get_previous_by_added(work)
    except Work.DoesNotExist:
        prev_work = None
    try:
        next_work = Work.get_next_by_added(work)
    except Work.DoesNotExist:
        next_work = None

    return render(request, "portfolio/work.html", locals())


def static_view(request, template):
    categs = Category.objects.all()
    work_cover = Work.objects.filter(bck=True).order_by('?').first()
    return render(request, template, locals())


def contact(request):
    return static_view(request, "portfolio/contact.html")


def labs(request):
    return static_view(request, "portfolio/labs.html")


# def create_error_view(code):
#     def error_view(request, *args, **kwargs):
#         barItems     = Category.objects.filter(menu=True)
#         moreBarItems = Category.objects.filter(menu=False)
#
#         coverImage = choice(Cover.objects.filter(pin=True))
#
#         response = render(request, "perso/error.html", locals())
#         response.status_code = code
#         return response
#     return error_view
