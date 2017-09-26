from django.db   import models
from django.urls import reverse


class Quote(models.Model):
    text   = models.TextField                (                                  verbose_name="texte")
    author = models.CharField                (max_length=64, default='Anonyme', verbose_name="auteur")
    year   = models.PositiveSmallIntegerField(               default=2016,      verbose_name="année") #TODO ranged YearField implementation
    added  = models.DateTimeField            (auto_now_add=True,                verbose_name="date d'ajout")

    def __str__(self):
        return "%s - %s" % (self.id, self.author)

    def get_absolute_url(self):
        return reverse('quotes:main', kwargs={'id': self.id})

    class Meta:
        verbose_name        = "citation"
