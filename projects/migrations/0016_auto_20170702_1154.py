# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20170702_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
