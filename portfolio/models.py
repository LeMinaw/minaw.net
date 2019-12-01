from django.db.models import (Model, DateTimeField, SlugField, CharField,
    ImageField, TextField, BooleanField, ManyToManyField, AutoField)
from django.urls import reverse
from colorthief import ColorThief
from .utils import rgb_to_hex, hex_to_rgb, alpha

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
    _palette  = CharField(max_length=64,    blank=True, verbose_name="palette")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:work', kwargs={'work_slug': self.slug})

    def get_svg_placeholder(self):
        return ('data:image/svg+xml,'
            '%3Csvg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {self.cover.width} {self.cover.height}"%3E%3C/svg%3E')
    
    def compute_color_palette(self):
        ct = ColorThief(self.cover)
        ct.image = ct.image.resize((100, 100))
        cols = ct.get_palette(3, quality=50)
        self._palette = ';'.join([str(rgb_to_hex(col[:3])) for col in cols])
        # super().save()
    
    def get_palette(self):
        if not self._palette:
            self.save() # To generate color palette
        palette = self._palette.split(';')
        return tuple([hex_to_rgb(hexcode) for hexcode in palette])
    
    def get_css_gradient(self):
        cols = self.get_palette()
        return ('background-image:'
            f'linear-gradient(000deg, {alpha(cols[0], 0.8)}, {alpha(cols[0], 0.2)} 60%),'
            f'linear-gradient(120deg, {alpha(cols[1], 0.8)}, {alpha(cols[1], 0.2)} 60%),'
            f'linear-gradient(240deg, {alpha(cols[2], 0.8)}, {alpha(cols[2], 0.2)} 60%);')
    
    def save(self, *args, **kwargs):
        self.compute_color_palette()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "réalisation"
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
