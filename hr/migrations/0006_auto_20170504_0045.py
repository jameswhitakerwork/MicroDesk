# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 00:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0005_auto_20170503_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_code',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Contract_Type'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Grade'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='monthly_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='total_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='expected_monthly_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_code',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='wbs',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]