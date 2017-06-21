#-*- coding: utf-8 -*-

from django.db   import models
from django.urls import reverse

class Publication(models.Model):
    added   = models.DateTimeField(auto_now_add=True, verbose_name="ajouté")
    modif   = models.DateTimeField(auto_now=True    , verbose_name="modifié")
    content = models.TextField(blank=True,    verbose_name="contenu")
    title   = models.CharField(max_length=64, verbose_name="titre")
    slug    = models.SlugField(               verbose_name="slug")
    categs  = models.ManyToManyField('Category')
    tags    = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('publication', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "publication"


class Category(models.Model):
    descr = models.TextField(blank=True,    verbose_name="description")
    name  = models.CharField(max_length=64, verbose_name="nom")
    slug  = models.SlugField(               verbose_name="slug")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "catégorie"


class Tag(models.Model):
    name  = models.CharField(max_length=16, verbose_name="nom")
    slug  = models.SlugField(               verbose_name="slug")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "étiquette"
