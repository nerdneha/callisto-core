# Generated by Django 2.0 on 2017-12-13 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("wizard_builder", "0045_auto_20171122_1808")]

    operations = [
        migrations.AddField(
            model_name="formquestion",
            name="skip_eval",
            field=models.BooleanField(default=True),
        )
    ]
