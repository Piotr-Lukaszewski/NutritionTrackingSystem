# Generated by Django 3.0.7 on 2020-08-13 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0002_auto_20200806_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3),
        ),
    ]
