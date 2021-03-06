# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 08:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employ', '0002_auto_20160710_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_profile',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='job_profile',
            name='created_by',
        ),
        migrations.AddField(
            model_name='employee',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employer',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
