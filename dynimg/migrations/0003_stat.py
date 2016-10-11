# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynimg', '0002_auto_20160522_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('displayedImgs', models.PositiveIntegerField()),
                ('registeredImgs', models.PositiveIntegerField()),
                ('registeredUrls', models.PositiveIntegerField()),
                ('processingTime', models.DurationField()),
            ],
        ),
    ]
