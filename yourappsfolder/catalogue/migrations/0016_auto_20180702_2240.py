# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 20:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_auto_20180702_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='new_field',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='newfield',
            new_name='subcategory',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='newnew_field',
            new_name='subsubcategory',
        ),
    ]
