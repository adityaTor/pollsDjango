# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 01:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addComment', '0006_auto_20161230_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='author',
        ),
    ]