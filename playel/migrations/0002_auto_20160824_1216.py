# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='inh_genres',
            field=models.BooleanField(default=True, verbose_name=b'Inherit from main album genres'),
        ),
        migrations.AlterField(
            model_name='album',
            name='aux_covers',
            field=models.ManyToManyField(related_name='album.aux_covers+', verbose_name=b'Auxiliary covers', to='playel.Cover', blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='pub_date',
            field=models.DateField(null=True, verbose_name=b'Publication date', blank=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='b_date',
            field=models.DateField(null=True, verbose_name=b'Birth date', blank=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='d_date',
            field=models.DateField(null=True, verbose_name=b'Death date', blank=True),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='b_date',
            field=models.DateField(null=True, verbose_name=b'Birth date', blank=True),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='d_date',
            field=models.DateField(null=True, verbose_name=b'Death date', blank=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='b_date',
            field=models.DateField(null=True, verbose_name=b'Birth date', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='aux_covers',
            field=models.ManyToManyField(related_name='track.aux_covers+', verbose_name=b'Auxiliary covers', to='playel.Cover', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='pub_date',
            field=models.DateField(null=True, verbose_name=b'Publication date', blank=True),
        ),
    ]
