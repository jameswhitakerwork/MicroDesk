# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 14:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20170131_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='expected_duration',
        ),
        migrations.RemoveField(
            model_name='position',
            name='total_expected_cost',
        ),
        migrations.AddField(
            model_name='contract',
            name='advanced_field_security',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='basic_field_security',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='duty_station_orientation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='iom_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='iom_un_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='medical_clearance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='personal_history',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='photo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='policy_and_conduct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='proof_of_life',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='ses_initiated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='travel_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contract',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='position',
            name='expected_need_ntil',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='reports_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Position'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address_1',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address_2',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address_3',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='duty_address_1',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='duty_address_2',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='duty_address_3',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='duty_zip_code',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='staff',
            name='home_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='home_phone_at_station',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='mobile_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='mobile_phone_at_station',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='staff',
            name='shirt_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Shirt_Size'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='un_warden_zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Warden_Zone'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staff',
            name='zip_code',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
