#-*- coding: utf-8 -*-

from django.urls import reverse
from django.db   import models
from datetime    import timedelta

class BaseModel(models.Model):
    created    = models.DateField    (auto_now_add=True,             verbose_name="création"             )
    last_used  = models.DateField    (auto_now=True,    blank=True,  verbose_name="dernière utilisation" )
    times_used = models.IntegerField (                  default=0,   verbose_name="nombre d'utilisations")

    class Meta:
        abstract = True


class ImageUrl(BaseModel):
    dwnlTime  = models.DurationField(default=timedelta(0),        verbose_name="temps de téléchargement")
    url       = models.URLField     (max_length=128, unique=True, verbose_name="URL"                    )

    def __str__(self):
        return self.url

    class Meta:
        verbose_name        = "URL d'image"
        verbose_name_plural = "URLs d'images"


class DynamicImg(BaseModel):
    name       = models.CharField      (max_length=32, blank=True, verbose_name="nom")
    urls       = models.ManyToManyField(ImageUrl,                  verbose_name="URLs")
    shadowMode = models.BooleanField   (default=False,             verbose_name="mode discret")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('dynimg:getimg', kwargs={'id_img': self.id})

    def get_urls_nb(self):
        return self.urls.count()
    get_urls_nb.short_description = "Nombre d'URLs"


    class Meta:
        verbose_name        = "image dynamique"
        verbose_name_plural = "images dynamiques"
