# Generated by Django 5.0.2 on 2024-03-01 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Supplier",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, null=True, unique=True)),
                ("address", models.CharField(blank=True, null=True)),
                ("includes_gst_in_prices", models.BooleanField()),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "supplier",
                "managed": False,
            },
        ),
    ]
