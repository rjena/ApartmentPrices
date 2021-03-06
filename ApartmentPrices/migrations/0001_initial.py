# Generated by Django 2.0.4 on 2018-05-29 18:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], verbose_name='Количество комнат')),
                ('area', models.PositiveIntegerField(default=50, validators=[django.core.validators.MinValueValidator(10)], verbose_name='Площадь')),
                ('first_floor', models.BooleanField(verbose_name='На 1-м этаже?')),
                ('last_floor', models.BooleanField(verbose_name='На последнем этаже?')),
                ('balcony', models.BooleanField(default=False, verbose_name='Есть балкон?')),
                ('total_floors', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Всего этажей')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_dstr', models.CharField(max_length=20, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_mtrl', models.CharField(max_length=20, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Материал дома',
                'verbose_name_plural': 'Материалы дома',
            },
        ),
        migrations.AddField(
            model_name='apartment',
            name='h_dstr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApartmentPrices.District', verbose_name='Район'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='h_mtrl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApartmentPrices.Material', verbose_name='Материал дома'),
        ),
    ]
