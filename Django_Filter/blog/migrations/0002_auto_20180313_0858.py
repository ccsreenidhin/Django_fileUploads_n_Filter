# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='tags',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
