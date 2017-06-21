# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descr', models.TextField(verbose_name=b'description', blank=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'nom')),
                ('slug', models.SlugField(verbose_name=b'slug')),
            ],
            options={
                'verbose_name': 'cat\xe9gorie',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name=b'ajout\xc3\xa9')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name=b'modifi\xc3\xa9')),
                ('content', models.TextField(verbose_name=b'contenu', blank=True)),
                ('title', models.CharField(max_length=64, verbose_name=b'titre')),
                ('slug', models.SlugField(verbose_name=b'slug')),
                ('categs', models.ManyToManyField(to='perso.Category')),
            ],
            options={
                'verbose_name': 'publication',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'nom')),
                ('slug', models.SlugField(verbose_name=b'slug')),
            ],
            options={
                'verbose_name': '\xe9tiquette',
            },
        ),
        migrations.AddField(
            model_name='publication',
            name='tags',
            field=models.ManyToManyField(to='perso.Tag'),
        ),
    ]
