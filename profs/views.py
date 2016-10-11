#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http      import HttpResponse
from profs.models     import *
from profs.forms      import *
from profs.processing import *


def main(request):
    return render(request, "profs/main.html", locals())


def about(request):
    return render(request, "profs/about.html", locals())


def contact(request):
    return render(request, "profs/contact.html", locals())


# @vary_on_headers('HTTP_X_REQUESTED_WITH') # Needed when using caching
def modules(request):
    semester, subject, teacher = None, None, None
    displayedModules = Module.objects.all()

    if request.method == "POST":
        form = ModulesForm(request.POST)
        if form.is_valid():
            semester = form.cleaned_data['semester']
            subject  = form.cleaned_data['subject']
            teacher  = form.cleaned_data['teacher']
            if semester != None:
                displayedModules = displayedModules.filter(semester=semester)
            if subject != None:
                displayedModules = displayedModules.filter(subject=subject)
            if teacher != None:
                displayedModules = displayedModules.filter(teacher=teacher)

            if request.is_ajax():
                xmlResponse = Taconite()

                xmlResponse.addClass("disabled", "#id_semester > [value=\"4\"]")

                xmlResponse.show(".collection > a")
                hiddenModules = Module.objects.exclude(id__in=displayedModules)
                for item in hiddenModules:
                    xmlResponse.hide(".collection > a[href=\"" + item.get_absolute_url() + "\"]")

                xmlResponse.js("$(\"select\").material_select();")

                return HttpResponse(xmlResponse, content_type="text/xml")

    else:
        form = ModulesForm()

    return render(request, "profs/modules.html", locals())


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
    else:
        form = AddCommentForm()

    return render(request, "profs/module.html", locals())
