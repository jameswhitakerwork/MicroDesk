# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 08:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0013_auto_20170423_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 4, 23, 8, 50, 22, 619718, tzinfo=utc), null=True),
        ),
    ]