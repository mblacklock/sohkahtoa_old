# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubtopicQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_of', models.IntegerField()),
                ('subtopic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='topics.Subtopic')),
            ],
        ),
    ]