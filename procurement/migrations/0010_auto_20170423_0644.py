# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 06:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0009_auto_20170423_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 4, 23, 6, 44, 56, 602433, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_justification',
            field=models.CharField(max_length=512),
        ),
    ]
