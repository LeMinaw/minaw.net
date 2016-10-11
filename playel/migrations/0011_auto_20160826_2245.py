# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0010_auto_20160825_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trackalbumrelation',
            options={'verbose_name': 'Relation piste-album', 'verbose_name_plural': 'Relations pistes-albums'},
        ),
        migrations.AlterField(
            model_name='trackalbumrelation',
            name='track_nb',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Num\xc3\xa9ro de piste'),
        ),
    ]
