# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 09:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20170702_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 2, 9, 54, 25, 41058, tzinfo=utc)),
        ),
    ]
