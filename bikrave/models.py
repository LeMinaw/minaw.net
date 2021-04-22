from django.db.models import (Model, DateTimeField, SlugField, CharField,
    ImageField, TextField, BooleanField, PositiveSmallIntegerField, ForeignKey, CASCADE)
from django.urls import reverse
from django.conf import settings
from datetime import date
import requests
import logging


logger = logging.getLogger('django')


class Work(Model):
    added  = DateTimeField(auto_now_add=True, verbose_name="ajouté")
    url    = CharField(max_length=128, verbose_name="URL")
    pin    = BooleanField(default=False, verbose_name="épinglé")
    author = ForeignKey('Artist', on_delete=CASCADE, related_name='works', verbose_name="auteur")

    # def __init__(self, *args, **kwargs):
    #     self._meta = None
    #     super(Work, self).__init__(*args, **kwargs)

    @property
    def name(self):
        return self.get_metadata()['title']
    
    @property
    def desc(self):
        return self.get_metadata()['description']
    
    @property
    def cover_url(self):
        return self.get_metadata()['artwork_url']
    
    @property
    def waveform_url(self):
        return self.get_metadata()['waveform_url']
    
    @property
    def genre(self):
        return self.get_metadata()['genre']

    @property
    def tags(self):
        return self.get_metadata()['tag_list'].split(' ')
    
    @property
    def released(self):
        meta = self.get_metadata()
        return date(year=meta['release_year'], month=meta['release_month'], day=meta['release_day'])
    
    def get_metadata(self):
        try:
            return self._metadata
        except AttributeError:
            logger.info("Fetching metadata: %s", self.url)
            rq = requests.get("http://api.soundcloud.com/resolve",
                    params={'url':self.url, 'client_id':settings.SND_CLIENT_ID})
            self._metadata = rq.json()
            return self._metadata

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bikrave:artist', kwargs={'slug': self.author.slug})

    class Meta:
        verbose_name = "oeuvre"
        ordering = ['-added']


class Artist(Model):
    name  = CharField(max_length=64, verbose_name="nom")
    slug  = SlugField(unique=True, verbose_name="identifiant")
    pic   = ImageField(verbose_name="logo")
    bio   = TextField(blank=True, default='', verbose_name="bio")
    quote = TextField(blank=True, default='', verbose_name="citation")
    index = PositiveSmallIntegerField(verbose_name="ordre")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bikrave:artist', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "artiste"
        ordering = ['index']
