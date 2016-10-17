#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http      import HttpResponse
from perso.models     import *
from perso.forms      import *

def main(request):
    return render(request, "perso/main.html", locals())

def publication(slug):
    pass

def category(slug):
    pass

def tag(slug):
    pass
