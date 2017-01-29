# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0013_auto_20160829_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='autors',
            field=models.ManyToManyField(verbose_name='Auteurs', blank=True, to='playel.Autor'),
        ),
        migrations.AlterField(
            model_name='album',
            name='aux_covers',
            field=models.ManyToManyField(verbose_name='Couvertures auxilliaires', blank=True, related_name='album.aux_covers+', to='playel.Cover'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(verbose_name='Couverture', blank=True, null=True, to='playel.Cover'),
        ),
        migrations.AlterField(
            model_name='album',
            name='desc',
            field=models.TextField(verbose_name='Description', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(verbose_name='Nom', max_length=64),
        ),
        migrations.AlterField(
            model_name='album',
            name='pub_date',
            field=models.DateField(verbose_name='Date de publication', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(verbose_name='Identifiant', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='tracks',
            field=models.ManyToManyField(verbose_name='Pistes', blank=True, to='playel.Track', through='playel.TrackAlbumRelation'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='b_date',
            field=models.DateField(verbose_name='Date de naissance', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='d_date',
            field=models.DateField(verbose_name='Date de mort', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='desc',
            field=models.TextField(verbose_name='Description', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='autor',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='name',
            field=models.CharField(verbose_name='Nom', max_length=64),
        ),
        migrations.AlterField(
            model_name='autor',
            name='slug',
            field=models.SlugField(verbose_name='Identifiant', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cover',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cover',
            name='cover_autors',
            field=models.ManyToManyField(verbose_name='Auteurs de couverture', blank=True, to='playel.CoverAutor'),
        ),
        migrations.AlterField(
            model_name='cover',
            name='desc',
            field=models.TextField(verbose_name='Description', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='cover',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='cover',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='cover',
            name='name',
            field=models.CharField(verbose_name='Nom', max_length=64),
        ),
        migrations.AlterField(
            model_name='cover',
            name='slug',
            field=models.SlugField(verbose_name='Identifiant', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='b_date',
            field=models.DateField(verbose_name='Date de naissance', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='d_date',
            field=models.DateField(verbose_name='Date de mort', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='desc',
            field=models.TextField(verbose_name='Description', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='name',
            field=models.CharField(verbose_name='Nom', max_length=64),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='slug',
            field=models.SlugField(verbose_name='Identifiant', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='genre',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='b_date',
            field=models.DateField(verbose_name='Date de naissance', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='desc',
            field=models.TextField(verbose_name='Description', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='genre',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(verbose_name='Nom', max_length=64),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(verbose_name='Identifiant', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='track',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='autors',
            field=models.ManyToManyField(verbose_name='Auteurs', blank=True, to='playel.Autor'),
        ),
        migrations.AlterField(
            model_name='track',
            name='aux_covers',
            field=models.ManyToManyField(verbose_name='Couvertures auxilliaires', blank=True, related_name='track.aux_covers+', to='playel.Cover'),
        ),
        migrations.AlterField(
            model_name='track',
            name='bpm',
            field=models.PositiveSmallIntegerField(verbose_name='BPM', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='cover',
            field=models.ForeignKey(verbose_name='Couverture', blank=True, null=True, to='playel.Cover'),
        ),
        migrations.AlterField(
            model_name='track',
            name='desc',
            field=models.TextField(verbose_name='Description', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.DurationField(verbose_name='Durée', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='file_mp3',
            field=models.FileField(verbose_name='Fichier MP3', blank=True, upload_to='tracks/ogg'),
        ),
        migrations.AlterField(
            model_name='track',
            name='file_ogg',
            field=models.FileField(verbose_name='Fichier OGG', blank=True, upload_to='tracks/mp3'),
        ),
        migrations.AlterField(
            model_name='track',
            name='inh_album',
            field=models.ForeignKey(verbose_name="Hériter des attributs de l'album", blank=True, null=True, to='playel.Album'),
        ),
        migrations.AlterField(
            model_name='track',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='name',
            field=models.CharField(verbose_name='Nom', max_length=64),
        ),
        migrations.AlterField(
            model_name='track',
            name='plays_nb',
            field=models.PositiveSmallIntegerField(verbose_name='Nombre de lectures', default=0),
        ),
        migrations.AlterField(
            model_name='track',
            name='pub_date',
            field=models.DateField(verbose_name='Date de publication', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='slug',
            field=models.SlugField(verbose_name='Identifiant', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trackalbumrelation',
            name='track',
            field=models.ForeignKey(verbose_name='Piste', to='playel.Track'),
        ),
        migrations.AlterField(
            model_name='trackalbumrelation',
            name='track_nb',
            field=models.PositiveSmallIntegerField(verbose_name='Numéro de piste', default=1),
        ),
    ]
