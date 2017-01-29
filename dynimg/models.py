#-*- coding: utf-8 -*-

from django.db import models
# from datetime  import timedelta

class Stat(models.Model):
    displayedImgs  = models.PositiveIntegerField(default=0)
    registeredImgs = models.PositiveIntegerField(default=0)
    registeredUrls = models.PositiveIntegerField(default=0)
    processingTime = models.DurationField       (default=0) # TODO Init default with timedelta(0), but problem in migration serialisation.
    def __str__(self):
        return "STATISTICS" # Stats is a special DB, all stats stored in first object (id=1)

class ImageUrl(models.Model):
    url        = models.URLField     (                         max_length=128,   unique=True)
    dwnlTime   = models.DurationField("Average download time", null=True,        blank=True )
    created    = models.DateField    (                         auto_now_add=True            )
    last_used  = models.DateField    (                         auto_now=True,    blank=True )
    times_used = models.IntegerField (                                           default=0  )
    def __str__(self):
        return self.url

class DynamicImg(models.Model):
    name       = models.CharField           (max_length=16,                   blank=True)
    urls       = models.ManyToManyField     (ImageUrl                                   )
    urls_nb    = models.PositiveIntegerField(                                           )
    created    = models.DateField           (               auto_now_add=True           )
    last_used  = models.DateField           (               auto_now=True,    blank=True)
    times_used = models.PositiveIntegerField(default=0                                  )
    shadowMode = models.BooleanField        (default=False                              )
    def __str__(self):
        return str(self.id)
