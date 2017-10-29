# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 23:56
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


def move_choice_question(apps, schema_editor):
    current_database = schema_editor.connection.alias
    Choice = apps.get_model('wizard_builder.Choice')
    for choice in Choice.objects.using(current_database):
        base_question = choice.question.formquestion_ptr
        choice.new_question = base_question
        choice.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wizard_builder', '0033_add_temps'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='new_question',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='example2',
                to='wizard_builder.FormQuestion'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='example1',
                to='wizard_builder.MultipleChoice'),
        ),
        migrations.RunPython(
            move_choice_question,
            migrations.RunPython.noop,
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='new_question',
            new_name='question',
        ),
    ]
