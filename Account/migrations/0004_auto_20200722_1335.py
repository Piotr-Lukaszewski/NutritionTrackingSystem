# Generated by Django 3.0.7 on 2020-07-22 11:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20200722_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproducts',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 7, 22, 11, 35, 15, 229191, tzinfo=utc)),
        ),
    ]
