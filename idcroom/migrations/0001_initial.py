# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idcroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('user', models.CharField(default='', max_length=255, verbose_name='\u64cd\u4f5c\u5458')),
                ('comment', models.TextField(default='', verbose_name='\u5907\u6ce8')),
            ],
        ),
    ]
