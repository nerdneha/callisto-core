# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("wizard_builder", "0019_remove_choice_extra_info_placeholder")]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="extra_info_text",
            field=models.TextField(blank=True),
        )
    ]
