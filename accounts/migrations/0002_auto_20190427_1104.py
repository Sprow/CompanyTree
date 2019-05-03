# Generated by Django 2.1.7 on 2019-04-27 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 4, 27, 11, 4, 41, 213410, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.FileField(blank=True, upload_to=utils.get_file_path),
        ),
    ]
