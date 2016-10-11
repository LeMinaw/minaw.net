# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynimg', '0004_auto_20160812_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='processingTime',
            field=models.DurationField(blank=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='registeredImgs',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='registeredUrls',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
