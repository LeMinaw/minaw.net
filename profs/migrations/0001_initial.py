# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9')),
                ('content', models.TextField(verbose_name=b'contenu')),
                ('author', models.CharField(max_length=32, verbose_name=b'auteur', blank=True)),
                ('validated', models.BooleanField(default=False, verbose_name=b'valid\xc3\xa9')),
            ],
            options={
                'verbose_name': 'avis',
                'verbose_name_plural': 'avis',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9')),
            ],
            options={
                'verbose_name': 'module',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9')),
                ('name', models.CharField(max_length=16, verbose_name=b'nom')),
                ('short', models.CharField(max_length=3, verbose_name=b'nom abr\xc3\xa9g\xc3\xa9')),
                ('slug', models.SlugField(verbose_name=b'slug')),
            ],
            options={
                'verbose_name': 'semestre',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9')),
                ('name', models.CharField(max_length=32, verbose_name=b'nom')),
                ('short', models.CharField(max_length=16, verbose_name=b'nom abr\xc3\xa9g\xc3\xa9')),
                ('slug', models.SlugField(verbose_name=b'slug')),
            ],
            options={
                'verbose_name': 'mati\xe8re',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name=b'Ajout\xc3\xa9')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name=b'Modifi\xc3\xa9')),
                ('name', models.CharField(max_length=32, verbose_name=b'nom')),
                ('short', models.CharField(max_length=16, verbose_name=b'nom abr\xc3\xa9g\xc3\xa9')),
                ('slug', models.SlugField(verbose_name=b'slug')),
            ],
            options={
                'verbose_name': 'enseignant',
            },
        ),
        migrations.AddField(
            model_name='module',
            name='semester',
            field=models.ForeignKey(verbose_name=b'semestre', to='profs.Semester', on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='module',
            name='subject',
            field=models.ForeignKey(verbose_name=b'mati\xc3\xa8re', to='profs.Subject', on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='module',
            name='teacher',
            field=models.ForeignKey(verbose_name=b'enseignant', to='profs.Teacher', on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='comment',
            name='module',
            field=models.ForeignKey(related_name='comments', verbose_name=b'module', to='profs.Module', on_delete=django.db.models.deletion.CASCADE),
        ),
    ]
