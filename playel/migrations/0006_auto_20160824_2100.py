# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0005_auto_20160824_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='aux_albums',
            field=models.ManyToManyField(related_name='track.aux_albums+', verbose_name=b'Albums auxilliaires', to='playel.Album', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='file_mp3',
            field=models.FileField(upload_to=b'tracks/ogg', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='file_ogg',
            field=models.FileField(upload_to=b'tracks/mp3', blank=True),
        ),
    ]
