# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('playel', '0004_auto_20160824_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='modif',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 18, 32, 29, 759782, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autor',
            name='modif',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 18, 33, 22, 726063, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cover',
            name='modif',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 18, 33, 36, 433996, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coverautor',
            name='modif',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 18, 33, 39, 821367, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='modif',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 18, 33, 42, 780268, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='modif',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 18, 33, 46, 210510, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
