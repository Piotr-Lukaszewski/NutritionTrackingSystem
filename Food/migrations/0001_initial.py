# Generated by Django 3.0.7 on 2020-08-06 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('protein', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('fat', models.FloatField()),
                ('quantity_per_portion', models.IntegerField(blank=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100)),
                ('food_type', models.CharField(blank=True, choices=[('1', 'Meat'), ('2', 'Fruit'), ('3', 'Vegetable'), ('4', 'SeaFood'), ('5', 'Nuts'), ('6', 'Grains'), ('7', 'Diary')], max_length=2)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ingredinet_based', models.BooleanField(default=False)),
                ('recipe', models.CharField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ReceipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food.Ingredient')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food.Product')),
            ],
            options={
                'verbose_name_plural': 'Receipe Ingredients',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='ingredient',
            field=models.ManyToManyField(through='Food.ReceipeIngredient', to='Food.Ingredient'),
        ),
    ]
