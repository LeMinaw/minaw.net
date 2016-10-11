# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('generatedSequences', models.IntegerField(verbose_name=b'Total des s\xc3\xa9quences g\xc3\xa9n\xc3\xa9r\xc3\xa9es')),
                ('generatedPages', models.IntegerField(verbose_name=b'Total des pages g\xc3\xa9n\xc3\xa9r\xc3\xa9es')),
                ('generationTime', models.DurationField(verbose_name=b'Total des temps de g\xc3\xa9n\xc3\xa9ration')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=32, verbose_name=b'Mot')),
                ('likes', models.IntegerField(verbose_name=b'Nombre de likes')),
                ('date', models.DateField(auto_now=True, verbose_name=b'Date du dernier like')),
            ],
        ),
    ]
