# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-16 12:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0015_auto_20170716_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lists_agented', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lists_owned', to=settings.AUTH_USER_MODEL),
        ),
    ]