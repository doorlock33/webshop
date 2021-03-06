# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0024_auto_20180702_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ean',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subsubcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productattributevalue',
            name='test',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
