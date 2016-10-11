# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0006_auto_20160824_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackAlbumRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('track_nb', models.PositiveSmallIntegerField(default=1)),
                ('album', models.ForeignKey(to='playel.Album')),
            ],
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.RemoveField(
            model_name='track',
            name='aux_albums',
        ),
        migrations.RemoveField(
            model_name='track',
            name='inh_autors',
        ),
        migrations.RemoveField(
            model_name='track',
            name='inh_genres',
        ),
        migrations.RemoveField(
            model_name='track',
            name='number',
        ),
        migrations.AddField(
            model_name='track',
            name='inh_album',
            field=models.ForeignKey(verbose_name=b"H\xc3\xa9riter des attributs de l'album", blank=True, to='playel.Album', null=True),
        ),
        migrations.AddField(
            model_name='trackalbumrelation',
            name='track',
            field=models.ForeignKey(to='playel.Track'),
        ),
        migrations.AddField(
            model_name='album',
            name='tracks',
            field=models.ManyToManyField(to='playel.Track', through='playel.TrackAlbumRelation', blank=True),
        ),
    ]
