# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 19:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0028_productattributevalue_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattributevalue',
            name='test',
        ),
    ]