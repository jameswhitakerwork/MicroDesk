# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_department_jsignaturemodel_mission_prstatus_purchaseitem_wbs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PRStatus',
        ),
        migrations.DeleteModel(
            name='PurchaseItem',
        ),
        migrations.DeleteModel(
            name='WBS',
        ),
    ]
