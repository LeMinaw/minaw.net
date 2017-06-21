# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profs', '0004_auto_20160925_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='short',
            field=models.CharField(max_length=4, verbose_name=b'nom abr\xc3\xa9g\xc3\xa9'),
        ),
    ]
