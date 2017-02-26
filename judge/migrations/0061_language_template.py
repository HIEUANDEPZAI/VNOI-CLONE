# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0060_contest_clarifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='template',
            field=models.TextField(blank=True, help_text='Code template to display in submission editor.', verbose_name='code template'),
        ),
    ]