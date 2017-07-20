#-*- coding: utf-8 -*-

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import HttpResponse
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO


def genErrImg(text="No further info"):
    """Generates an error reporting image."""

    img = Image.open(static("dynimg/img/Error.png"))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(static("dynimg/font/ubuntu.ttf"), 15)
    draw.text((0, 235), "Err: %s" % text, (20, 20, 20), font=font)
    return img


def imgHttpResponse(img):
    """Generates an appropriate HttpResponse object from a PIL image."""

    img_io = BytesIO()
    img.save(img_io, format='PNG')
    img_file = ContentFile(img_io.getvalue())
    return HttpResponse(img_file, content_type="image/png")
