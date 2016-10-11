# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, blank=True)),
                ('urls_nb', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('last_used', models.DateField(auto_now=True)),
                ('times_used', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ImageUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(unique=True, max_length=128)),
                ('dwnlTime', models.DurationField(verbose_name=b'Average download time', blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('last_used', models.DateField(auto_now=True)),
                ('times_used', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='dynamicimg',
            name='urls',
            field=models.ManyToManyField(to='dynimg.ImageUrl'),
        ),
    ]
