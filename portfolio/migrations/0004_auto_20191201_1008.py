# Generated by Django 2.2.5 on 2019-12-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20191201_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='_palette',
            field=models.CharField(blank=True, max_length=64, verbose_name='palette'),
        ),
    ]