# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 05:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0022_auto_20170506_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 6, 5, 5, 58, 335013, tzinfo=utc)),
        ),
    ]
