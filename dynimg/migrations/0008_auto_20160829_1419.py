# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynimg', '0007_auto_20160812_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicimg',
            name='shadowMode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stat',
            name='displayedImgs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stat',
            name='processingTime',
            field=models.DurationField(default=0),
        ),
        migrations.AlterField(
            model_name='stat',
            name='registeredImgs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stat',
            name='registeredUrls',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
