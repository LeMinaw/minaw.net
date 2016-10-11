# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('pub_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('b_date', models.DateField(null=True, blank=True)),
                ('d_date', models.DateField(null=True, blank=True)),
                ('autors', models.ManyToManyField(related_name='autors_rel_+', to='playel.Autor', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(null=True, upload_to=b'covers', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoverAutor',
            fields=[
                ('added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('b_date', models.DateField(null=True, blank=True)),
                ('d_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('b_date', models.DateField(null=True, blank=True)),
                ('parent_genres', models.ManyToManyField(to='playel.Genre', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('file_ogg', models.FileField(upload_to=b'tracks/mp3')),
                ('file_mp3', models.FileField(upload_to=b'tracks/ogg')),
                ('number', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=64)),
                ('pub_date', models.DateField(null=True, blank=True)),
                ('duration', models.DurationField(null=True, blank=True)),
                ('bpm', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('plays_nb', models.PositiveSmallIntegerField(default=0)),
                ('album', models.ForeignKey(blank=True, to='playel.Album', null=True)),
                ('autors', models.ManyToManyField(to='playel.Autor', blank=True)),
                ('aux_covers', models.ManyToManyField(related_name='track.aux_covers+', to='playel.Cover', blank=True)),
                ('cover', models.ForeignKey(blank=True, to='playel.Cover', null=True)),
                ('genres', models.ManyToManyField(to='playel.Genre', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cover',
            name='cover_autors',
            field=models.ManyToManyField(to='playel.CoverAutor', blank=True),
        ),
        migrations.AddField(
            model_name='autor',
            name='genres',
            field=models.ManyToManyField(to='playel.Genre', blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='autors',
            field=models.ManyToManyField(to='playel.Autor', blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='aux_covers',
            field=models.ManyToManyField(related_name='album.aux_covers+', to='playel.Cover', blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(blank=True, to='playel.Cover', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='genres',
            field=models.ManyToManyField(to='playel.Genre', blank=True),
        ),
    ]
