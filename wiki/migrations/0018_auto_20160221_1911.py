# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0017_message_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255, verbose_name='Auteur')),
                ('newContent', models.TextField(verbose_name='Contenu modifié')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='lastModification',
        ),
        migrations.AddField(
            model_name='modification',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Article', verbose_name='Article réfèrant'),
        ),
    ]
