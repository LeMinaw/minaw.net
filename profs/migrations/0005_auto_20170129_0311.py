# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profs', '0004_auto_20160925_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'module', 'ordering': ['semester', 'subject', 'teacher']},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'enseignant', 'ordering': ['slug']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(verbose_name='auteur', max_length=32, default=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='contenu'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='module',
            field=models.ForeignKey(verbose_name='module', related_name='comments', to='profs.Module'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='validated',
            field=models.BooleanField(verbose_name='validé', default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='year',
            field=models.PositiveSmallIntegerField(verbose_name='année', default=2016),
        ),
        migrations.AlterField(
            model_name='module',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='content',
            field=models.TextField(verbose_name='contenu', blank=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='semester',
            field=models.ForeignKey(verbose_name='semestre', to='profs.Semester'),
        ),
        migrations.AlterField(
            model_name='module',
            name='subject',
            field=models.ForeignKey(verbose_name='matière', to='profs.Subject'),
        ),
        migrations.AlterField(
            model_name='module',
            name='teacher',
            field=models.ForeignKey(verbose_name='enseignant', to='profs.Teacher'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(verbose_name='nom', max_length=16),
        ),
        migrations.AlterField(
            model_name='semester',
            name='short',
            field=models.CharField(verbose_name='nom abrégé', max_length=4),
        ),
        migrations.AlterField(
            model_name='semester',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(verbose_name='nom', max_length=32),
        ),
        migrations.AlterField(
            model_name='subject',
            name='short',
            field=models.CharField(verbose_name='nom abrégé', max_length=16),
        ),
        migrations.AlterField(
            model_name='subject',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='added',
            field=models.DateTimeField(verbose_name='Ajouté', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='modif',
            field=models.DateTimeField(verbose_name='Modifié', auto_now=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(verbose_name='nom', max_length=32),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='short',
            field=models.CharField(verbose_name='nom abrégé', max_length=16),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterIndexTogether(
            name='module',
            index_together=set([('semester', 'subject', 'teacher')]),
        ),
    ]
