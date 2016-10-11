# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0008_auto_20160825_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackalbumrelation',
            name='track_nb',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
