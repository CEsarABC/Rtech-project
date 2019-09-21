# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-08 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicesUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('project_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.project')),
            ],
        ),
    ]