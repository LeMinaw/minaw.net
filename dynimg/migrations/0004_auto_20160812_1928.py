# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynimg', '0003_stat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='displayedImgs',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
