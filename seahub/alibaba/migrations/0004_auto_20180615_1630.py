# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-15 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0003_auto_20180615_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicate',
            name='is_consumed',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='communicate',
            name='topic',
            field=models.CharField(db_index=True, max_length=64),
        ),
    ]
