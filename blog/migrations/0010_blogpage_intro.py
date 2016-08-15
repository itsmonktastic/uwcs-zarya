# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-14 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='intro',
            field=models.TextField(blank=True, max_length=500, verbose_name='This is displayed on the home and blog listing pages'),
        ),
    ]