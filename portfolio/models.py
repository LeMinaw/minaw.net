from django.db.models import (Model, DateTimeField, SlugField,
    CharField, TextField, BooleanField, ManyToManyField,
    AutoField, PositiveSmallIntegerField)
from sorl.thumbnail import ImageField
from django.db.models.signals import post_init
from django.urls import reverse
from colorthief import ColorThief
from .utils import rgb_to_hex, hex_to_rgb, alpha
from PIL import Image


class Work(Model):
    added     = DateTimeField(auto_now_add=True,                          verbose_name="ajouté")
    modif     = DateTimeField(auto_now=True,                              verbose_name="modifié")
    slug      = SlugField(unique=True,                                    verbose_name="identifiant")
    title     = CharField(max_length=64,                                  verbose_name="titre")
    subtitle  = CharField(max_length=128,            blank=True,          verbose_name="sous-titre")
    cover     = ImageField(                                               verbose_name="couverture")
    cover_w   = PositiveSmallIntegerField(null=True, blank=True,          verbose_name="largeur couverture")
    cover_h   = PositiveSmallIntegerField(null=True, blank=True,          verbose_name="hauteur couverture")
    content   = TextField(                           blank=True,          verbose_name="contenu")
    bck       = BooleanField(default=False,                               verbose_name="arrière-plan")
    pin       = BooleanField(default=False,                               verbose_name="épinglé")
    black_txt = BooleanField(default=False,                               verbose_name="texte noir")
    categ     = ManyToManyField('Category',          blank=True,          verbose_name="catégorie")
    _palette  = CharField(max_length=64,             blank=True,          verbose_name="palette")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:work', kwargs={'work_slug': self.slug})
    
    def get_cover_dimensions(self):
        if self.cover_w is None or self.cover_h is None:
            self.cover_w = self.cover.width
            self.cover_h = self.cover.height
            self.save(compute_palette=False, compute_dimensions=False)
        return self.cover_w, self.cover_h

    def get_svg_placeholder(self):
        w, h = self.get_cover_dimensions()
        return ('data:image/svg+xml,'
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"></svg>'
        )
    
    def compute_color_palette(self):
        self.cover.open() # Fixes a bug in file handling due to w/h update
        thumb = Image.open(self.cover).resize((100, 100))
        ct = ColorThief(thumb, is_obj=True)
        try:
            cols = ct.get_palette(3, ignore_black=False, quality=50)
        except Exception: # NoQA
            cols = ((255, 255, 255), (200, 200, 200), (220, 220, 220))
        while len(cols) < 3:
            cols.append(cols[0])
        self._palette = ';'.join([str(rgb_to_hex(col[:3])) for col in cols])
    
    def get_palette(self):
        if not self._palette:
            self.compute_color_palette()
            self.save(compute_palette=False) # To generate color palette
        palette = self._palette.split(';')
        return tuple([hex_to_rgb(hexcode) for hexcode in palette])
    
    def get_css_gradient(self):
        cols = self.get_palette()
        return ('background-image:'
            f'linear-gradient(000deg, {alpha(cols[0], 0.8)}, {alpha(cols[0], 0.2)} 60%),'
            f'linear-gradient(120deg, {alpha(cols[1], 0.8)}, {alpha(cols[1], 0.2)} 60%),'
            f'linear-gradient(240deg, {alpha(cols[2], 0.8)}, {alpha(cols[2], 0.2)} 60%);')
    
    def save(self, compute_palette=True, compute_dimensions=True, *args, **kwargs):
        if compute_palette:
            self.compute_color_palette()
        if compute_dimensions:
            self.get_cover_dimensions()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "réalisation"
        ordering = ['-pin', '-added']

# Needed to fix a hudge performance issue related to S3 storage.
# Work model implements its own logic to access cover dimensions.
post_init.disconnect(ImageField.update_dimension_fields)


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
