# Generated by Django 2.2.2 on 2019-08-04 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikrave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='bikrave.Artist', verbose_name='auteur'),
        ),
    ]
