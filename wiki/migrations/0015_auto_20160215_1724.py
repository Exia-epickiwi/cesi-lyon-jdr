# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0014_comment_replyto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='replyTo',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
