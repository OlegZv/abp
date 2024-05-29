# Generated by Django 4.2.11 on 2024-05-13 15:33

import django_jsonform.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0012_campaign_donation_action_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="newsletter_action",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="campaign",
            name="newsletter_cta",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="campaign",
            name="newsletter_tags",
            field=django_jsonform.models.fields.JSONField(blank=True, null=True),
        ),
    ]