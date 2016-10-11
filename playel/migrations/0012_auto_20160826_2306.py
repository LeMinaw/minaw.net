# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0011_auto_20160826_2245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Auteur'},
        ),
        migrations.AlterModelOptions(
            name='cover',
            options={'verbose_name': 'Couverture'},
        ),
        migrations.AlterModelOptions(
            name='coverautor',
            options={'verbose_name': 'Auteur de couverture', 'verbose_name_plural': 'Auteurs de couverture'},
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'verbose_name': 'Piste'},
        ),
        migrations.RemoveField(
            model_name='autor',
            name='autors',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='genres',
        ),
        migrations.AlterField(
            model_name='album',
            name='added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='album',
            name='autors',
            field=models.ManyToManyField(to='playel.Autor', verbose_name=b'Auteurs', blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(verbose_name=b'Couverture', blank=True, to='playel.Cover', null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='modif',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'Nom'),
        ),
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(serialize=False, verbose_name=b'Identifiant', primary_key=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='tracks',
            field=models.ManyToManyField(to='playel.Track', verbose_name=b'Pistes', through='playel.TrackAlbumRelation', blank=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='modif',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'Nom'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='slug',
            field=models.SlugField(serialize=False, verbose_name=b'Identifiant', primary_key=True),
        ),
        migrations.AlterField(
            model_name='cover',
            name='added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='cover',
            name='cover_autors',
            field=models.ManyToManyField(to='playel.CoverAutor', verbose_name=b'Auteurs de couverture', blank=True),
        ),
        migrations.AlterField(
            model_name='cover',
            name='modif',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='cover',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'Nom'),
        ),
        migrations.AlterField(
            model_name='cover',
            name='slug',
            field=models.SlugField(serialize=False, verbose_name=b'Identifiant', primary_key=True),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='modif',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'Nom'),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='slug',
            field=models.SlugField(serialize=False, verbose_name=b'Identifiant', primary_key=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='modif',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'Nom'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(serialize=False, verbose_name=b'Identifiant', primary_key=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='track',
            name='autors',
            field=models.ManyToManyField(to='playel.Autor', verbose_name=b'Auteurs', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='bpm',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'BPM', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='cover',
            field=models.ForeignKey(verbose_name=b'Couverture', blank=True, to='playel.Cover', null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.DurationField(null=True, verbose_name=b'Dur\xc3\xa9e', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='file_mp3',
            field=models.FileField(upload_to=b'tracks/ogg', verbose_name=b'Fichier MP3', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='file_ogg',
            field=models.FileField(upload_to=b'tracks/mp3', verbose_name=b'Fichier OGG', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='modif',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='track',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'Nom'),
        ),
        migrations.AlterField(
            model_name='track',
            name='plays_nb',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'Nombre de lectures'),
        ),
        migrations.AlterField(
            model_name='track',
            name='slug',
            field=models.SlugField(serialize=False, verbose_name=b'Identifiant', primary_key=True),
        ),
        migrations.AlterField(
            model_name='trackalbumrelation',
            name='track',
            field=models.ForeignKey(verbose_name=b'Piste', to='playel.Track'),
        ),
    ]
