# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-14 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160814_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=models.TextField(blank=True, help_text='This is displayed on the home and blog listing pages'),
        ),
    ]
