# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-09 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoodRecipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
