# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-20 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20170915_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='subscription',
            field=models.BooleanField(default=False),
        ),
    ]
