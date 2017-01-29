# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynimg', '0008_auto_20160829_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageurl',
            name='dwnlTime',
            field=models.DurationField(verbose_name='Average download time', blank=True, null=True),
        ),
    ]
