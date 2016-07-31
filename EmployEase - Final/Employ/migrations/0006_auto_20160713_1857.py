# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-13 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employ', '0005_auto_20160713_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_profile',
            name='preferred_time',
            field=models.CharField(choices=[('MORNING', 'MORNING'), ('AFTERNOON', 'AFTERNOON'), ('EVENING', 'EVENING'), ('NIGHT', 'NIGHT'), ('ANY', 'ANYTIME')], max_length=15),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='qualifications',
            field=models.CharField(choices=[('10th pass', '10th pass'), ('12th pass', '12th pass'), ('U_G', 'Under Grdauate'), ('P_G', 'Post Graduate'), ('NON', 'None')], max_length=10),
        ),
        migrations.AlterField(
            model_name='job_profile',
            name='preferred_time',
            field=models.CharField(choices=[('MORNING', 'MORNING'), ('AFTERNOON', 'AFTERNOON'), ('EVENING', 'EVENING'), ('NIGHT', 'NIGHT'), ('ANY', 'ANYTIME')], max_length=15),
        ),
        migrations.AlterField(
            model_name='job_profile',
            name='qualifications',
            field=models.CharField(choices=[('10th pass', '10th pass'), ('12th pass', '12th pass'), ('U_G', 'Under Grdauate'), ('P_G', 'Post Graduate'), ('NON', 'None')], max_length=10),
        ),
    ]
