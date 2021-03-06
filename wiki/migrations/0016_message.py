# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0015_auto_20160215_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255, verbose_name='Auteur')),
                ('content', models.TextField(verbose_name='Contenu')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Article', verbose_name='Article associé')),
            ],
        ),
    ]
