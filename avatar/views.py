from django.urls              import reverse
from django.http              import HttpResponse
from django.shortcuts         import render
from django.core.files.base   import ContentFile
from django.core.files.images import ImageFile
from io                       import BytesIO
from hashlib                  import md5
from avatar.forms             import *
from avatar.processing        import *


def main(request):
    if request.method == "POST":
        form = TestForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            emailHash = md5(email.strip().lower().encode()).hexdigest()
            avatarUrl = reverse('avatar:getimg', kwargs={'id_img': emailHash, 'size': 400})

            if request.is_ajax():
                xmlResponse = Taconite()
                xmlResponse.replace("#testImg", "<img id='testImg' src='%s'></img>" % avatarUrl)
                return HttpResponse(xmlResponse, content_type="text/xml")

    else:
        form = TestForm()

    return render(request, "avatar/main.html", locals())


def getimg(request, id_img, size=128):
    img = genAvatar(id_img, min(int(size), 512))
    img_io = BytesIO()
    img.save(img_io, format='PNG')
    img_file = ContentFile(img_io.getvalue())
    return HttpResponse(img_file, content_type="image/png")


def about(request):
    return render(request, "avatar/about.html", locals())
