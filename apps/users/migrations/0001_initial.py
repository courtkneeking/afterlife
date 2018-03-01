# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-19 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funeral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funeral_location', models.CharField(max_length=100)),
                ('funeral_address', models.CharField(max_length=100)),
                ('funeral_date', models.CharField(max_length=100)),
                ('funeral_info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('death_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='funeral',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Subject'),
        ),
    ]