# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0003_auto_20160824_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='desc',
            field=models.TextField(default=b'', verbose_name=b'Description', blank=True),
        ),
        migrations.AddField(
            model_name='autor',
            name='desc',
            field=models.TextField(default=b'', verbose_name=b'Description', blank=True),
        ),
        migrations.AddField(
            model_name='cover',
            name='desc',
            field=models.TextField(default=b'', verbose_name=b'Description', blank=True),
        ),
        migrations.AddField(
            model_name='coverautor',
            name='desc',
            field=models.TextField(default=b'', verbose_name=b'Description', blank=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='desc',
            field=models.TextField(default=b'', verbose_name=b'Description', blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='desc',
            field=models.TextField(default=b'', verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='pub_date',
            field=models.DateField(null=True, verbose_name=b'Date de publication', blank=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='b_date',
            field=models.DateField(null=True, verbose_name=b'Date de naissance', blank=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='d_date',
            field=models.DateField(null=True, verbose_name=b'Date de mort', blank=True),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='b_date',
            field=models.DateField(null=True, verbose_name=b'Date de naissance', blank=True),
        ),
        migrations.AlterField(
            model_name='coverautor',
            name='d_date',
            field=models.DateField(null=True, verbose_name=b'Date de mort', blank=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='b_date',
            field=models.DateField(null=True, verbose_name=b'Date de naissance', blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='pub_date',
            field=models.DateField(null=True, verbose_name=b'Date de publication', blank=True),
        ),
    ]
