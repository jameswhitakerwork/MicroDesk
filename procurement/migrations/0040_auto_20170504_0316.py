# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 03:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0039_auto_20170504_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsignaturemodel',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 4, 3, 16, 36, 676185, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 4, 3, 16, 36, 677205, tzinfo=utc), null=True),
        ),
    ]