# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 10:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0016_auto_20170423_0852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchaserequest',
            options={'permissions': (('can_confirm_need', 'Can confirm need'), ('can_confirm_funds_available', 'Can confirm funds available'), ('can_give_final_approval_low_value', 'Can give final approval for low value PRs'), ('can_give_final_approval_high_value', 'Can give final approval for high value PRs'))},
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 4, 23, 10, 3, 3, 251483, tzinfo=utc), null=True),
        ),
    ]