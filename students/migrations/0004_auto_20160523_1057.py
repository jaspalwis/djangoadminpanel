# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 05:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20160523_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
