# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employ', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('PIN', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('PIN', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='job_profile',
            name='description',
        ),
        migrations.AddField(
            model_name='job_profile',
            name='salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee_profile',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employ.Employee'),
        ),
        migrations.AlterField(
            model_name='job_profile',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='job_profile',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Employ.Employer'),
        ),
    ]