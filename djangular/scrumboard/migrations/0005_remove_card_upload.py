# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-06-23 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0004_card_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='upload',
        ),
    ]
