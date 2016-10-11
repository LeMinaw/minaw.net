# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0009_auto_20160825_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trackalbumrelation',
            options={'verbose_name': 'piste'},
        ),
    ]
