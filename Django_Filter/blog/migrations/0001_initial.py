# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 08:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('domain', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('image', models.FileField(blank=True, null=True, upload_to='media/')),
                ('reviews', models.IntegerField(default=0)),
                ('discription', models.TextField(blank=True, max_length=500)),
                ('tags', models.CharField(blank=True, max_length=20, null=True)),
                ('categories', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('sub_loc', models.CharField(blank=True, max_length=20, null=True)),
                ('popularity', models.IntegerField(default=0)),
                ('trending', models.IntegerField(default=0)),
            ],
        ),
    ]
