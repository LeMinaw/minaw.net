#-*- coding: utf-8 -*-

from django.db   import models
from django.urls import reverse


class MainModel(models.Model):
    added = models.DateTimeField (auto_now_add=True     , verbose_name="Ajouté")
    modif = models.DateTimeField (auto_now=True         , verbose_name="Modifié")
    name  = models.CharField     (max_length=64         , verbose_name="Nom")
    slug  = models.SlugField     (primary_key=True      , verbose_name="Identifiant")
    desc  = models.TextField     (blank=True, default='', verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Track(MainModel):
    autors     = models.ManyToManyField           ('Autor', blank=True                                      , verbose_name="Auteurs")
    genres     = models.ManyToManyField           ('Genre', blank=True                                      )
    cover      = models.ForeignKey                ('Cover', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Couverture")
    pub_date   = models.DateField                 (         blank=True, null=True                           , verbose_name="Date de publication")
    aux_covers = models.ManyToManyField           ('Cover', blank=True, related_name='track.aux_covers+'    , verbose_name="Couvertures auxilliaires")
    inh_album  = models.ForeignKey                ('Album', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Hériter des attributs de l'album")
    file_ogg   = models.FileField                 (         blank=True, upload_to='tracks/mp3'              , verbose_name="Fichier OGG")
    file_mp3   = models.FileField                 (         blank=True, upload_to='tracks/ogg'              , verbose_name="Fichier MP3")
    duration   = models.DurationField             (         blank=True, null=True                           , verbose_name="Durée")
    bpm        = models.PositiveSmallIntegerField (         blank=True, null=True                           , verbose_name="BPM")
    plays_nb   = models.PositiveSmallIntegerField (                     default=0                           , verbose_name="Nombre de lectures")

    def iautors(self):
        '''Returns a QuerySet of autors, considering inheritance.'''
        if self.inh_album != None and self.autors == None:
            return self.inh_album.autors.all()
        return self.autors.all()

    def igenres(self):
        '''Returns a QuerySet of genres, considering inheritance.'''
        if self.inh_album != None and self.genres == None:
            return self.inh_album.genres.all()
        return self.genres.all()

    def icover(self):
        '''Returns cover, considering inheritance.'''
        if self.inh_album != None and self.cover == None:
            return self.inh_album.cover
        return self.cover

    def ipub_date(self):
        '''Returns pub_date, considering inheritance.'''
        if self.inh_album != None and self.pub_date == None:
            return self.inh_album.pub_date
        return self.pub_date

    def iaux_covers(self):
        '''Returns a QuerySet of aux_covers, considering inheritance.'''
        if self.inh_album != None and self.aux_covers == None:
            return self.inh_album.aux_covers.all()
        return self.aux_covers.all()

    def get_absolute_url(self):
        return reverse('playel.views.track', kwargs={'track_id': self.slug})

    class Meta:
        verbose_name = "Piste"


class Album(MainModel):
    tracks     = models.ManyToManyField ('Track', blank=True, through='TrackAlbumRelation'        , verbose_name="Pistes")
    genres     = models.ManyToManyField ('Genre', blank=True                                      )
    autors     = models.ManyToManyField ('Autor', blank=True                                      , verbose_name="Auteurs")
    cover      = models.ForeignKey      ('Cover', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Couverture")
    aux_covers = models.ManyToManyField ('Cover', blank=True, related_name='album.aux_covers+'    , verbose_name="Couvertures auxilliaires")
    pub_date   = models.DateField       (         blank=True, null=True                           , verbose_name="Date de publication")

    def plays_nb(self):
        '''Sums plays number of all the tracks the album contains.'''
        plays_nb = 0
        for track in self.track_set.all():
            plays_nb += track.plays_nb
        return plays_nb

    def duration(self):
        '''Sums durations of all the tracks the album contains.'''
        duration = 0
        for track in self.track_set.all():
            duration += track.duration
        return duration

    def get_absolute_url(self):
        return reverse('playel.views.album', kwargs={'album_id': self.slug})


class Autor(MainModel):
  # genres = models.ManyToManyField ('Genre',   blank=True)
  # autors = models.ManyToManyField ('self',    blank=True, verbose_name="Auteurs")
    b_date = models.DateField       (null=True, blank=True, verbose_name="Date de naissance")
    d_date = models.DateField       (null=True, blank=True, verbose_name="Date de mort")

    def plays_nb(self):
        '''Sums plays number of all the tracks the album contains.'''
        plays_nb = 0
        for track in self.track_set.all():
            plays_nb += track.plays_nb
        return plays_nb

    def get_absolute_url(self):
        return reverse('playel.views.autor', kwargs={'autor_id': self.slug})

    class Meta:
        verbose_name = "Auteur"


class Genre(MainModel):
    parent_genres = models.ManyToManyField ('self', blank=True, symmetrical=False) #TODO Bug lors de la migration quand on met un verbose name
    b_date        = models.DateField       (        blank=True, null=True        , verbose_name="Date de naissance")

    def get_absolute_url(self):
        return reverse('playel.views.genre', kwargs={'track_id': self.slug})

class Cover(MainModel):
    image = models.ImageField             (upload_to='covers', null=True, blank=True)
    cover_autors = models.ManyToManyField ('CoverAutor',                  blank=True, verbose_name="Auteurs de couverture")

    def get_absolute_url(self):
        return reverse('playel.views.cover', kwargs={'track_id': self.slug})

    class Meta:
        verbose_name = "Couverture"


class CoverAutor(MainModel):
    b_date = models.DateField (null=True, blank=True, verbose_name="Date de naissance")
    d_date = models.DateField (null=True, blank=True, verbose_name="Date de mort")

    class Meta:
        verbose_name = "Auteur de couverture"
        verbose_name_plural = "Auteurs de couverture"


class TrackAlbumRelation(models.Model):
    track    = models.ForeignKey                ('Track', on_delete=models.CASCADE, verbose_name="Piste")
    album    = models.ForeignKey                ('Album', on_delete=models.CASCADE)
    track_nb = models.PositiveSmallIntegerField (         default=1               , verbose_name="Numéro de piste")

    def __str__(self):
        return self.track.name + ' dans ' + self.album.name

    class Meta:
        verbose_name = "Relation piste-album"
        verbose_name_plural = "Relations pistes-albums"
        ordering = ['track_nb']
