# Generated by Django 3.1.3 on 2020-11-09 11:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naamvinder', '0004_auto_20201109_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='deelnemers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), size=7),
        ),
    ]
