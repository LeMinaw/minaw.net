# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0012_auto_20160826_2306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trackalbumrelation',
            options={'ordering': ['track_nb'], 'verbose_name': 'Relation piste-album', 'verbose_name_plural': 'Relations pistes-albums'},
        ),
    ]
