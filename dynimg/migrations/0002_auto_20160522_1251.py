# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynimg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageurl',
            name='dwnlTime',
            field=models.DurationField(null=True, verbose_name=b'Average download time', blank=True),
        ),
    ]
