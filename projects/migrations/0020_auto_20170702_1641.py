# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20170702_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='projects/steeps/'),
        ),
    ]
