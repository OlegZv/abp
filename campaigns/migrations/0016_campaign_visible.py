# Generated by Django 4.2.13 on 2024-09-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0015_petitionsignature_newsletter_opt_in"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="visible",
            field=models.BooleanField(default=True),
        ),
    ]