# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-08 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0004_fundvaluecalc_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('value', models.FloatField()),
            ],
        ),
    ]
