# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('first_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=30)),
                ('inum', models.IntegerField()),
            ],
        ),
    ]
