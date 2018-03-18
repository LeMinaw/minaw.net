#-*- coding: utf-8 -*-

from django.db   import models
from django.urls import reverse
from hashlib import md5

class Publication(models.Model):
    added    = models.DateTimeField(auto_now_add=True, verbose_name="ajouté")
    modif    = models.DateTimeField(auto_now=True    , verbose_name="modifié")
    slug     = models.SlugField()
    cover    = models.ForeignKey('Cover', null=True, blank=True, on_delete=models.CASCADE, verbose_name="couverture")
    title    = models.CharField(max_length=64,  verbose_name="titre")
    subtitle = models.CharField(max_length=128, blank=True, verbose_name="sous-titre")
    content  = models.TextField(blank=True,     verbose_name="contenu")
    abstract = models.TextField(blank=True,     verbose_name="résumé")
    pin      = models.BooleanField(default=False, verbose_name="épinglé")
    categ    = models.ForeignKey('Category', null=True, on_delete=models.CASCADE, verbose_name="catégorie")
    tags     = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('perso:publication', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "publication"
        ordering = ['-added']


class Category(models.Model):
    id    = models.AutoField(primary_key=True)
    descr = models.TextField(blank=True,    verbose_name="description")
    name  = models.CharField(max_length=64, verbose_name="nom")
    menu  = models.BooleanField(default=True)
    slug  = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('perso:main', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "catégorie"
        ordering = ['menu', 'id']


class Tag(models.Model):
    name  = models.CharField(max_length=16, verbose_name="nom")
    slug  = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('perso:tag', kwargs={'slug': self.slug})

    def get_occurences(self):
        return self.publication_set.count()

    class Meta:
        verbose_name = "étiquette"


class Comment(models.Model):
    added   = models.DateTimeField(auto_now_add=True, verbose_name="ajouté")
    pseudo  = models.CharField(max_length=64)
    email   = models.EmailField(blank=True)
    content = models.TextField(verbose_name="contenu")
    publi   = models.ForeignKey('Publication', on_delete=models.CASCADE, verbose_name="publication")

    def __str__(self):
        return str(self.publi) + ' - ' + str(self.id)

    def get_absolute_url(self):
        return reverse('perso:tag', kwargs={'slug': self.slug})

    def get_avatar_url(self, size=90):
        if self.email != '':
            uid = md5(self.email.lower().encode()).hexdigest()
        else:
            uid = md5(self.pseudo.lower().encode()).hexdigest()
        return "https://www.gravatar.com/avatar/%(uid)s?s=%(size)s&d=http://minaw.net/avatar/i/%(uid)s/%(size)s" % {'uid':uid, 'size':size}

    class Meta:
        verbose_name = "commentaire"
        ordering = ['-added']


class Cover(models.Model):
    name  = models.CharField(max_length=64, verbose_name="nom")
    image = models.ImageField()
    descr = models.TextField(blank=True,    verbose_name="description")
    pin   = models.BooleanField(default=False, verbose_name="épinglé")
    blackOverlay = models.BooleanField(default=False, verbose_name="surimpression noire")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "couverture"


class Subscription(models.Model):
    added = models.DateTimeField(auto_now_add=True, verbose_name="ajouté")
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "souscription"
