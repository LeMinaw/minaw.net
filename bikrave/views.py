from django.shortcuts import render
from django.http      import Http404
from bikrave.models import Work, Artist


def main(request):
    return render(request, 'bikrave/main.html', locals())
    
def sound(request):
    categ = 'sound'
    return render(request, 'bikrave/sound.html', locals())

def prod(request):
    categ = 'prod'
    artists = Artist.objects.all()
    return render(request, 'bikrave/prod.html', locals())

def artist(request, slug):
    artist = Artist.objects.get(slug=slug)
    return render(request, 'bikrave/artist.html', locals())
    