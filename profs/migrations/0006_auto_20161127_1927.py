# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profs', '0005_auto_20161017_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['semester', 'subject', 'teacher'], 'verbose_name': 'module'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['slug'], 'verbose_name': 'enseignant'},
        ),
    ]
