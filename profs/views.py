#-*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts             import render
from django.http                  import HttpResponse
from profs.processing             import *
from profs.models                 import *
from profs.forms                  import *


def main(request):
    return render(request, "profs/main.html", locals())


def about(request):
    return render(request, "profs/about.html", locals())


def contact(request):
    return render(request, "profs/contact.html", locals())


@csrf_exempt
# @vary_on_headers('HTTP_X_REQUESTED_WITH') # Needed when using caching
def modules(request):
    displayedModules = Module.objects.all()

    if request.method == "POST":
        form = ModulesForm(request.POST)
        if form.is_valid():
            semester = Semester.objects.filter(name=form.cleaned_data['semester']) or Semester.objects.all()
            subject  = Subject.objects.filter(name=form.cleaned_data['subject']) or Subject.objects.all()
            teacher  = Teacher.objects.filter(name=form.cleaned_data['teacher'])  or Teacher.objects.all()

            displayedModules = displayedModules.filter(semester__in=semester, subject__in=subject, teacher__in=teacher)

            if request.is_ajax():
                xmlResponse = Taconite()

                xmlResponse.show(".collection > a")
                hiddenModules = Module.objects.exclude(id__in=displayedModules)
                for module in hiddenModules:
                    xmlResponse.hide(".collection > a[href=\"" + module.get_absolute_url() + "\"]")

                for isemester in Semester.objects.all(): # TODO: Factorisation
                    result = Module.objects.filter(semester=isemester, subject__in=subject, teacher__in=teacher).exists()
                    xmlResponse.disable("#id_semester > [value=\"" + str(isemester.id) + "\"]", not result)

                for isubject in Subject.objects.all():
                    result = Module.objects.filter(semester__in=semester, subject=isubject, teacher__in=teacher).exists()
                    xmlResponse.disable("#id_subject > [value=\"" + str(isubject.id) + "\"]", not result)

                for iteacher in Teacher.objects.all():
                    result = Module.objects.filter(semester__in=semester, subject__in=subject, teacher=iteacher).exists()
                    xmlResponse.disable("#id_teacher > [value=\"" + str(iteacher.id) + "\"]", not result)

                xmlResponse.js("$(\"select\").material_select();")

                return HttpResponse(xmlResponse, content_type="text/xml")

    else:
        form = ModulesForm()

    return render(request, "profs/modules.html", locals())


@csrf_exempt
def module(request, semester, subject, teacher):
    semester = Semester.objects.get(slug=semester)
    subject  = Subject.objects.get(slug=subject)
    teacher  = Teacher.objects.get(slug=teacher)

    module = Module.objects.get(semester=semester, subject=subject, teacher=teacher)
    comments = module.comments.all().filter(validated=True)

    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False) # form is a ModelForm
            new_comment.module = module
            new_comment.save()
            thanks = createThanks()
    else:
        form = AddCommentForm()

    return render(request, "profs/module.html", locals())
