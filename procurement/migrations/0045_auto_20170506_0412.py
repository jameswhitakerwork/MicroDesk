# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 04:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0044_auto_20170504_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsignaturemodel',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 6, 4, 12, 32, 719725, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 6, 4, 12, 32, 720843, tzinfo=utc), null=True),
        ),
    ]
