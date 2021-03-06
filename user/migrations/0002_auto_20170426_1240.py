# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 11:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Occcupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occcupation', models.CharField(choices=[('barber', 'Barber'), ('electrian', 'Electrian'), ('mechanic', 'Mechanic'), ('caterer', 'Caterer'), ('hair_dresser', 'Hair_dresser'), ('plumber', 'Plumber'), ('painter', 'Painter'), ('carpenter', 'Carpenter'), ('welder', 'Welder'), ('others', 'Others')], max_length=40)),
                ('skill', models.CharField(max_length=120)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Company'),
        ),
    ]
