# Generated by Django 2.0.1 on 2018-01-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("wizard_builder", "0047_remove_formquestion_skip_eval"),
    ]

    operations = [
        migrations.AddField(
            model_name="formquestion",
            name="sites",
            field=models.ManyToManyField(to="sites.Site"),
        )
    ]
