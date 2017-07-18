#-*- coding: utf-8 -*-

import re
from django import template
from perso.models import Cover

register = template.Library()

def img_repl(tag_match):
    """Replaces [img]data[/img] with a convenant HTML tag."""

    reg = re.compile(r'^\[img\]([^|]+)\|?([^|]+)?\[\/img\]$')
    cover_name = re.match(reg, tag_match.group(0)).group(1)
    css_class = re.match(reg, tag_match.group(0)).group(2)
    try:
        cover = Cover.objects.get(name=cover_name)
    except Cover.DoesNotExist:
        return "<p>Erreur : %s n'existe pas.</p>" % cover_name
    return "<img src=\"%s\" alt=\"%s\" class=\"%s\"/>" % (cover.image.url, cover.descr, css_class)


@register.filter(name='img')
def img(text):
    """A filter to allow models images integration in some raw text."""

    reg = re.compile(r'(\[img\].+\[\/img\])', re.M)
    return re.sub(reg, img_repl, text)
