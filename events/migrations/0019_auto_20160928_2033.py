# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 20:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20160922_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 28, 21, 33, 28, 47978, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='signup_close',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 28, 21, 33, 28, 48224, tzinfo=utc)),
        ),
    ]