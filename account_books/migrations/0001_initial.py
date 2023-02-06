# Generated by Django 4.1.6 on 2023-02-06 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountBook",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("amount", models.IntegerField()),
                ("memo", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account_details",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
