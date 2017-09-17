# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 05:49
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170829_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ntypes', to='news.NewsTypes'),
        ),
    ]
