# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-09 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_twitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='page_json',
            field=models.TextField(default='', max_length=8000),
        ),
        migrations.AlterField(
            model_name='pages',
            name='page_posts_json',
            field=models.TextField(default='', max_length=8000),
        ),
        migrations.AlterField(
            model_name='twitter',
            name='twitter_json',
            field=models.TextField(default='', max_length=8000),
        ),
    ]
