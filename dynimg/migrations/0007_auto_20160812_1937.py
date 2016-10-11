# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynimg', '0006_auto_20160812_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='displayedImgs',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='stat',
            name='processingTime',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='stat',
            name='registeredImgs',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='stat',
            name='registeredUrls',
            field=models.PositiveIntegerField(),
        ),
    ]
