# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('category', models.CharField(default=b'General', max_length=10)),
                ('email', models.CharField(max_length=150)),
                ('comment', models.CharField(max_length=600)),
                ('is_read', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['created_on'],
                'db_table': 'feedback',
            },
        ),
    ]
