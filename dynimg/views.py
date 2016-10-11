#-*- coding: utf-8 -*-

from django.shortcuts         import render
from django.http              import HttpResponse, HttpResponseRedirect
from django.core.files.images import ImageFile
from django.core.files.temp   import NamedTemporaryFile
from django.conf              import settings
from urllib2                  import urlopen, HTTPError, URLError
from random                   import randint
from sys                      import exc_info
from re                       import search
from dynimg.models            import *
from dynimg.forms             import *
from dynimg.processing        import *

def main(request):
    if request.method == "POST":
        form = NewImageForm(request.POST)
        
        if form.is_valid():
            name_new = form.cleaned_data['name']
            urls_new = form.cleaned_data['urls'].splitlines()
            
            image_db = DynamicImg(name=name_new, urls_nb=len(urls_new))
            
            for i in range(0, len(urls_new)):
                try:
                    url_db = ImageUrl.objects.get(url=urls_new[i]) #TODO Switch to getOrCreate
                except ImageUrl.DoesNotExist:
                    url_db = ImageUrl(url=urls_new[i])
                    url_db.save()
                image_db.save()
                image_db.urls.add(url_db) # We add url_db to image_db URLs
            
            image_id = image_db.id
            image_db.save()
            
            host = request.get_host()
            
            stats = Stat.objects.get_or_create(id=1)[0] # Stat is a special DB, all stats stored in first object (id=1)
            stats.registeredImgs += 1
            stats.registeredUrls += len(urls_new)
            stats.save()
    
    else:
        form = NewImageForm()
    
    return render(request, "dynimg/main.html", locals())


def getimg(request, id_img):
    try:
        image = DynamicImg.objects.get(id=id_img)
    except:
        exception = search("'(.*)'", str(exc_info()[0])).group(1) # Ugly code to get exception name
        genErrImg(exception)
        return HttpResponseRedirect('http://' + request.get_host() + settings.STATIC_URL + 'dynimg/img/' + exception + '.png')
    
    image.times_used += 1
    image.save()
    urls = image.urls.all()
    imageUrl = urls[randint(0, image.urls_nb-1)] # Choosing an URL randomly from provided URLs list
    imageUrl.times_used += 1
    imageUrl.save()
    url = imageUrl.url
    
    stats = Stat.objects.get(id=1) # Stat is a special DB, all stats stored in first object (id=1)
    stats.displayedImgs += 1
    stats.save()
    
    try:
        if image.shadowMode == True:
            imgtmp = NamedTemporaryFile(delete=True)
            imgtmp.write(urlopen(url).read())
            imgtmp.flush()
            img = ImageFile(imgtmp)
            return HttpResponse(img, content_type="image/jpeg") # Works with PNG
            
        else:
            return HttpResponseRedirect(url)
    
    except:
        exception = search("'(.*)'", str(exc_info()[0])).group(1) # Ugly code to get exception name
        genErrImg(exception)
        return HttpResponseRedirect('http://' + request.get_host() + settings.STATIC_URL + 'dynimg/img/' + exception + '.png')


def about(request):
    stats = Stat.objects.get(id=1) # Stat is a special DB, all stats stored in first object (id=1)
    displayedImgs  = stats.displayedImgs
    registeredImgs = stats.registeredImgs
    registeredUrls = stats.registeredUrls
    processingTime = stats.processingTime
    
    return render(request, "dynimg/about.html", locals())

def contact(request):
    return render(request, "dynimg/contact.html", locals())
