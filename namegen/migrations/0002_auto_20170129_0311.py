# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('namegen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='generatedPages',
            field=models.IntegerField(verbose_name='Total des pages générées'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='generatedSequences',
            field=models.IntegerField(verbose_name='Total des séquences générées'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='generationTime',
            field=models.DurationField(verbose_name='Total des temps de génération'),
        ),
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.DateField(verbose_name='Date du dernier like', auto_now=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='likes',
            field=models.IntegerField(verbose_name='Nombre de likes'),
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(verbose_name='Mot', max_length=32),
        ),
    ]
