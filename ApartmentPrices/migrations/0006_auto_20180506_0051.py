# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-05 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApartmentPrices', '0005_auto_20180426_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='area',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='total_floors',
        ),
    ]