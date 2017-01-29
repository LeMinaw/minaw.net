#-*- coding: utf-8 -*-

from django.shortcuts   import render
from django.http        import HttpResponse
from namegen.forms      import ParamsForm
from namegen.processing import generateSentence
from namegen.models     import *
from datetime           import timedelta

def main(request):
    if request.method == "POST":
        form = ParamsForm(request.POST)

        if form.is_valid():
            partsNb =    form.cleaned_data['partsNb']
            maxPartsNb = form.cleaned_data['maxPartsNb']
            minPartsNb = form.cleaned_data['minPartsNb']
            paretoDist = form.cleaned_data['paretoDist']
            onlyOnce =   form.cleaned_data['onlyOnce']
            addVoyels =  form.cleaned_data['addVoyels']
            wordsNb =    form.cleaned_data['wordsNb']

            generated = generateSentence(partsNb, maxPartsNb, minPartsNb, paretoDist, onlyOnce, addVoyels, wordsNb)

            results      = generated[0]
            deltatime    = generated[1]
            totalPartsNb = generated[2]
            totalRolls   = generated[3]

            stats = Stats.objects.get(id=1) # Stats is a special DB, all stats stored in first object (id=1)
            stats.generatedSequences += totalRolls
            stats.generatedPages += 1
            stats.generationTime += timedelta(milliseconds=deltatime)
            stats.save()

            return render(request, "namegen/main.html", locals())
    else:
        form = ParamsForm()

    return render(request, "namegen/main.html", locals())


def like(request):
    if request.POST.get('clicked', default=False):
        resultclicked = request.POST.get('resultclicked')

        try:
            word = Word.objects.get(word=resultclicked)
        except Word.DoesNotExist:
            word = Word(word = resultclicked, likes = 0)
        word.likes += 1
        word.save()

    return HttpResponse(status=200)


def about(request):
    stats = Stats.objects.get(id=1) # Stats is a special DB, all stats stored in first object (id=1)
    generatedSequences = stats.generatedSequences
    generatedPages     = stats.generatedPages
    generationTime     = stats.generationTime

    return render(request, "namegen/about.html", locals())


def top(request):
    words = Word.objects.order_by('-likes', 'date')
    top = []
    for i in range(0, 10):
        if i <= len(words)-1:
            top.append(words[i])
        else:
            break

    return render(request, "namegen/top.html", locals())
