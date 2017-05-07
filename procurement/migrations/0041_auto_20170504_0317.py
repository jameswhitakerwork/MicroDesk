# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 03:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0040_auto_20170504_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsignaturemodel',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 4, 3, 17, 7, 626088, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 4, 3, 17, 7, 627159, tzinfo=utc), null=True),
        ),
    ]
