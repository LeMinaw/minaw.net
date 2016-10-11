# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0002_auto_20160824_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='inh_autors',
            field=models.BooleanField(default=True, verbose_name=b"H\xc3\xa9riter des auteurs de l'album principal"),
        ),
        migrations.AlterField(
            model_name='album',
            name='aux_covers',
            field=models.ManyToManyField(related_name='album.aux_covers+', verbose_name=b'Couvertures auxilliaires', to='playel.Cover', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='aux_covers',
            field=models.ManyToManyField(related_name='track.aux_covers+', verbose_name=b'Couvertures auxilliaires', to='playel.Cover', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='inh_genres',
            field=models.BooleanField(default=True, verbose_name=b"H\xc3\xa9riter des genres de l'album principal"),
        ),
    ]
