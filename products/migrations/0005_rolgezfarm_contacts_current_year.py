# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170904_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='rolgezfarm_contacts',
            name='current_year',
            field=models.CharField(default='2017', max_length=10),
        ),
    ]
