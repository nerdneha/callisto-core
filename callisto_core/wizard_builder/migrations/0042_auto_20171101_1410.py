# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 14:10
from __future__ import unicode_literals

from django.db import migrations, models

import callisto_core.wizard_builder.model_helpers


class Migration(migrations.Migration):

    dependencies = [("wizard_builder", "0041_remove_formquestion_is_dropdown")]

    operations = [
        migrations.AlterField(
            model_name="choice",
            name="extra_info_text",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="choice", name="text", field=models.TextField(null=True)
        ),
    ]
