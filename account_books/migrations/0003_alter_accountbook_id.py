# Generated by Django 4.1.6 on 2023-02-08 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account_books", "0002_alter_accountbook_memo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountbook",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]