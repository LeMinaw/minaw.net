from django.db.models import (Model, DateTimeField, SlugField, CharField,
    ImageField, TextField, BooleanField, ManyToManyField, AutoField)
from django.urls import reverse

class Work(Model):
    added     = DateTimeField(auto_now_add=True,        verbose_name="ajouté")
    modif     = DateTimeField(auto_now=True,            verbose_name="modifié")
    slug      = SlugField(unique=True,                  verbose_name="identifiant")
    title     = CharField(max_length=64,                verbose_name="titre")
    subtitle  = CharField(max_length=128,   blank=True, verbose_name="sous-titre")
    cover     = ImageField(                             verbose_name="couverture")
    content   = TextField(                  blank=True, verbose_name="contenu")
    bck       = BooleanField(default=False,             verbose_name="arrière-plan")
    pin       = BooleanField(default=False,             verbose_name="épinglé")
    black_txt = BooleanField(default=False,             verbose_name="texte noir")
    categ     = ManyToManyField('Category', blank=True, verbose_name="catégorie")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:work', kwargs={'work_slug': self.slug})

    class Meta:
        verbose_name = "oeuvre"
        ordering = ['-pin', '-added']


class Category(Model):
    id    = AutoField(primary_key=True, verbose_name="numéro")
    name  = CharField(max_length=64,    verbose_name="nom")
    slug  = SlugField(                  verbose_name="identifiant")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:main', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "catégorie"
        ordering = ['id']
