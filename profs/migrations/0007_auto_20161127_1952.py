# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profs', '0006_auto_20161127_1927'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='module',
            index_together=set([('semester', 'subject', 'teacher')]),
        ),
    ]
