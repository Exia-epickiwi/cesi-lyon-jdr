# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0013_remove_comment_replyto'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replyTo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wiki.Comment'),
            preserve_default=False,
        ),
    ]
