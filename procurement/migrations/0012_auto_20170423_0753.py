# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 07:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0011_auto_20170423_0738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseitem',
            old_name='pr_no',
            new_name='pr',
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 4, 23, 7, 53, 9, 23180, tzinfo=utc), null=True),
        ),
    ]
