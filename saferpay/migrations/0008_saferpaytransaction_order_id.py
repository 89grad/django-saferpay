# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-11 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saferpay', '0007_auto_20180911_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saferpaytransaction',
            name='order_id',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
