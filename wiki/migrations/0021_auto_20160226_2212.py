# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0020_auto_20160224_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Article', verbose_name=b'Article associ\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='modification',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Article', verbose_name=b'Article r\xc3\xa9f\xc3\xa8rant'),
        ),
        migrations.AlterField(
            model_name='modification',
            name='newContent',
            field=models.TextField(verbose_name=b'Contenu modifi\xc3\xa9'),
        ),
    ]
