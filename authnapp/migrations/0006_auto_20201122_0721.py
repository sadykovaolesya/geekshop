# Generated by Django 2.2.16 on 2020-11-22 07:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0005_create_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 7, 21, 22, 696051, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
