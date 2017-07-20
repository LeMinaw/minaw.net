#-*- coding: utf-8 -*-

from django.core.files.images import ImageFile
from django.core.files.temp   import NamedTemporaryFile
from django.shortcuts         import render
from django.http              import HttpResponse, HttpResponseRedirect
from django.db.models         import Sum
from urllib.request           import urlopen
from random                   import choice
from sys                      import exc_info
from re                       import search
from dynimg.models            import *
from dynimg.forms             import *
from dynimg.processing        import *

def main(request):
    if request.method == "POST":
        form = NewImageForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            urls = form.cleaned_data['urls'].splitlines()

            image = DynamicImg(name=name)
            image.save()
            for url in urls:
                url_obj = ImageUrl.objects.get_or_create(url=url)[0]
                image.urls.add(url_obj)
            image.save()

    else:
        form = NewImageForm()

    return render(request, "dynimg/main.html", locals())


def getimg(request, id_img):
    try:
        image = DynamicImg.objects.get(id=id_img)
    except:
        exception = search("'(.*)'", str(exc_info()[0])).group(1) # Ugly code to get exception name
        return imgHttpResponse(genErrImg(exception))

    image.times_used += 1
    image.save()
    imageUrl = choice(image.urls.all()) # Choosing an URL randomly from provided URLs list
    imageUrl.times_used += 1
    imageUrl.save()

    if image.shadowMode:
        try:
            imgtmp = NamedTemporaryFile(delete=True)
            imgtmp.write(urlopen(url).read())
            imgtmp.flush()
            img = ImageFile(imgtmp)
            return HttpResponse(img, content_type="image/jpeg") # Works with PNG
        except:
            exception = search("'(.*)'", str(exc_info()[0])).group(1) # Ugly code to get exception name
            return imgHttpResponse(genErrImg(exception))

    else:
        return HttpResponseRedirect(imageUrl.url)


def about(request):
    registeredImgs = DynamicImg.objects.count()
    registeredUrls = ImageUrl.objects.count()
    displayedImgs = DynamicImg.objects.aggregate(Sum('times_used'))['times_used__sum']

    return render(request, "dynimg/about.html", locals())
