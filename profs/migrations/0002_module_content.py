# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='content',
            field=models.TextField(verbose_name=b'contenu', blank=True),
        ),
    ]
