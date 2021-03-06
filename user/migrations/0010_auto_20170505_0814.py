# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20170501_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='courtesy_rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='number_of_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='overall_rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='price_rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='quality_rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0),
        ),
    ]
