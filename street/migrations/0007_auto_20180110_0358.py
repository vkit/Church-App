# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-10 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('street', '0006_auto_20180110_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='allow_notification',
            field=models.IntegerField(blank=True, default=1, help_text='1-ON,2-OFF', null=True),
        ),
    ]
