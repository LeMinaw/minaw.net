# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profs', '0002_module_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='year',
            field=models.PositiveSmallIntegerField(default=2016, verbose_name=b'ann\xc3\xa9e'),
        ),
    ]
