# Generated by Django 4.2.9 on 2024-03-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
        ("campaigns", "0005_petition_email_body_petition_email_include_comment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="events",
            field=models.ManyToManyField(blank=True, null=True, to="events.scheduledevent"),
        ),
    ]