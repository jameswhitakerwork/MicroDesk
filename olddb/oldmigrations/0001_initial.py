# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 13:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_history', models.BooleanField()),
                ('medical_clearance', models.BooleanField()),
                ('policy_and_conduct', models.BooleanField()),
                ('iom_email', models.BooleanField()),
                ('basic_field_security', models.BooleanField()),
                ('advanced_field_security', models.BooleanField()),
                ('travel_profile', models.BooleanField()),
                ('proof_of_life', models.BooleanField()),
                ('ses_initiated', models.BooleanField()),
                ('duty_station_orientation', models.BooleanField()),
                ('photo', models.BooleanField()),
                ('iom_un_id', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_code', models.CharField(max_length=16)),
                ('file', models.FileField(blank=True, upload_to=b'')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('monthly_rate', models.IntegerField()),
                ('total_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_code', models.CharField(max_length=16)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('tor', models.CharField(max_length=1024)),
                ('start_date', models.DateField()),
                ('expected_need_ntil', models.DateField(blank=True)),
                ('expected_duration', models.DurationField()),
                ('expected_monthly_rate', models.IntegerField()),
                ('total_expected_cost', models.IntegerField()),
                ('wbs', models.CharField(max_length=32)),
                ('reports_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Position')),
            ],
        ),
        migrations.CreateModel(
            name='Simple_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=16)),
                ('staff_id', models.CharField(max_length=16)),
                ('personnel_no', models.CharField(max_length=16)),
                ('entry_on_duty', models.DateField(blank=True)),
                ('no_of_dependants', models.IntegerField()),
                ('file', models.FileField(blank=True, upload_to=b'')),
                ('photo', models.ImageField(blank=True, upload_to=b'')),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('personal_email', models.EmailField(blank=True, max_length=254)),
                ('home_phone', models.IntegerField(blank=True)),
                ('mobile_phone', models.IntegerField(blank=True)),
                ('home_phone_at_station', models.IntegerField(blank=True)),
                ('mobile_phone_at_station', models.IntegerField(blank=True)),
                ('address_1', models.CharField(blank=True, max_length=64)),
                ('address_2', models.CharField(blank=True, max_length=64)),
                ('address_3', models.CharField(blank=True, max_length=64)),
                ('address_country', django_countries.fields.CountryField(max_length=2)),
                ('zip_code', models.CharField(blank=True, max_length=8)),
                ('duty_address_1', models.CharField(blank=True, max_length=64)),
                ('duty_address_2', models.CharField(blank=True, max_length=64)),
                ('duty_address_3', models.CharField(blank=True, max_length=64)),
                ('duty_address_country', django_countries.fields.CountryField(max_length=2)),
                ('duty_zip_code', models.CharField(blank=True, max_length=8)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('simple_model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.Simple_Model')),
            ],
            bases=('hr.simple_model',),
        ),
        migrations.CreateModel(
            name='Contract_Type',
            fields=[
                ('simple_model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.Simple_Model')),
            ],
            bases=('hr.simple_model',),
        ),
        migrations.CreateModel(
            name='Duty_Station',
            fields=[
                ('simple_model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.Simple_Model')),
            ],
            bases=('hr.simple_model',),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('simple_model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.Simple_Model')),
            ],
            bases=('hr.simple_model',),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('simple_model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.Simple_Model')),
            ],
            bases=('hr.simple_model',),
        ),
        migrations.CreateModel(
            name='Position_Status',
            fields=[
                ('simple_model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.Simple_Model')),
            ],
            bases=('hr.simple_model',),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('simple_model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.Simple_Model')),
            ],
            bases=('hr.simple_model',),
        ),
        migrations.CreateModel(
            name='Shirt_Size',
            fields=[
                ('simple_model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.Simple_Model')),
            ],
            bases=('hr.simple_model',),
        ),
        migrations.CreateModel(
            name='Staff_Type',
            fields=[
                ('simple_model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.Simple_Model')),
            ],
            bases=('hr.simple_model',),
        ),
        migrations.CreateModel(
            name='Warden_Zone',
            fields=[
                ('simple_model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr.Simple_Model')),
            ],
            bases=('hr.simple_model',),
        ),
        migrations.AddField(
            model_name='contract',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Position'),
        ),
        migrations.AddField(
            model_name='contract',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Staff'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Contract'),
        ),
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Gender'),
        ),
        migrations.AddField(
            model_name='staff',
            name='shirt_size',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Shirt_Size'),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Staff_Type'),
        ),
        migrations.AddField(
            model_name='staff',
            name='un_warden_zone',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Warden_Zone'),
        ),
        migrations.AddField(
            model_name='position',
            name='duty_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Duty_Station'),
        ),
        migrations.AddField(
            model_name='position',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Program'),
        ),
        migrations.AddField(
            model_name='position',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Position_Status'),
        ),
        migrations.AddField(
            model_name='contract',
            name='action_after_expiration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Action'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Contract_Type'),
        ),
        migrations.AddField(
            model_name='contract',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Grade'),
        ),
    ]