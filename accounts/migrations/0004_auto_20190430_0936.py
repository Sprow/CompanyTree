# Generated by Django 2.1.7 on 2019-04-30 09:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190427_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 4, 30, 9, 36, 5, 134186, tzinfo=utc), null=True),
        ),
    ]
