# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-07 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
