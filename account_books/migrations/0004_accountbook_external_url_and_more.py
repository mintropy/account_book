# Generated by Django 4.1.6 on 2023-02-09 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account_books", "0003_alter_accountbook_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="accountbook",
            name="external_url",
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="accountbook",
            name="external_url_expire",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
