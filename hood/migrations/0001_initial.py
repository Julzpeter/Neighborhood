# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-06 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100, null=True)),
                ('posted_by', models.CharField(max_length=100, null=True)),
                ('count', models.CharField(max_length=100)),
                ('police', models.CharField(max_length=100)),
                ('police_department_address', models.CharField(max_length=100)),
                ('health', models.CharField(max_length=100)),
                ('health_department_address', models.CharField(max_length=100)),
            ],
        ),
    ]
