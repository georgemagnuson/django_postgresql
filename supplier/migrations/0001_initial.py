# Generated by Django 5.0.2 on 2024-03-03 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Invoice",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("invoice_date", models.DateField()),
                ("invoice_supplier_uuid", models.UUIDField(blank=True, null=True)),
                ("invoice_number", models.CharField()),
                (
                    "invoice_amount_gross",
                    models.DecimalField(
                        blank=True, decimal_places=65535, max_digits=65535, null=True
                    ),
                ),
                (
                    "invoice_amount_gst",
                    models.DecimalField(
                        blank=True, decimal_places=65535, max_digits=65535, null=True
                    ),
                ),
                (
                    "invoice_amount_net",
                    models.DecimalField(
                        blank=True, decimal_places=65535, max_digits=65535, null=True
                    ),
                ),
                ("invoice_credit", models.BooleanField(blank=True, null=True)),
                ("deleted_row", models.BooleanField(blank=True, null=True)),
            ],
            options={
                "db_table": "invoice",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Invoiceentry",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("gmail_message_id", models.CharField(blank=True, null=True)),
                ("entry_supplieritem_code", models.CharField(blank=True, null=True)),
                (
                    "entry_supplieritem_description",
                    models.CharField(blank=True, null=True),
                ),
                (
                    "entry_qty",
                    models.DecimalField(
                        blank=True, decimal_places=65535, max_digits=65535, null=True
                    ),
                ),
                ("entry_unit_of_purchase", models.CharField(blank=True, null=True)),
                (
                    "entry_price",
                    models.DecimalField(
                        blank=True, decimal_places=65535, max_digits=65535, null=True
                    ),
                ),
                (
                    "entry_discount",
                    models.DecimalField(
                        blank=True, decimal_places=65535, max_digits=65535, null=True
                    ),
                ),
                (
                    "entry_gross_weight",
                    models.DecimalField(
                        blank=True, decimal_places=65535, max_digits=65535, null=True
                    ),
                ),
                (
                    "entry_net_weight",
                    models.DecimalField(
                        blank=True, decimal_places=65535, max_digits=65535, null=True
                    ),
                ),
                (
                    "entry_number_of_pieces",
                    models.DecimalField(
                        blank=True, decimal_places=65535, max_digits=65535, null=True
                    ),
                ),
                ("deleted_row", models.BooleanField(blank=True, null=True)),
                ("supplier_uuid", models.UUIDField(blank=True, null=True)),
                ("supplieritem_uuid", models.UUIDField(blank=True, null=True)),
                (
                    "entry_waste_weight",
                    models.DecimalField(
                        blank=True, decimal_places=65535, max_digits=65535, null=True
                    ),
                ),
            ],
            options={
                "db_table": "invoiceentry",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                (
                    "gmail_message_id",
                    models.CharField(blank=True, null=True, unique=True),
                ),
                ("message_date", models.DateField(blank=True, null=True)),
                ("message_from", models.CharField(blank=True, null=True)),
                ("message_to", models.CharField(blank=True, null=True)),
                ("message_subject", models.CharField(blank=True, null=True)),
                ("message_raw", models.CharField(blank=True, null=True)),
                (
                    "deleted_row",
                    models.BooleanField(
                        blank=True,
                        db_comment="instead of deleting just check this",
                        null=True,
                    ),
                ),
                ("message_has_attachments", models.BooleanField(blank=True, null=True)),
                ("message_processed", models.BooleanField(blank=True, null=True)),
                ("message_status", models.CharField(blank=True, null=True)),
            ],
            options={
                "db_table": "message",
                "managed": False,
            },
        ),
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
        migrations.CreateModel(
            name="Supplieritem",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("deleted_row", models.BooleanField(blank=True, null=True)),
                (
                    "supplieritem_code",
                    models.CharField(
                        blank=True, db_column="supplier_item_code", null=True
                    ),
                ),
                ("supplieritem_description", models.CharField(blank=True, null=True)),
                ("unit_of_purchase", models.CharField(blank=True, null=True)),
                (
                    "quantity_unit_of_purchase_in_unit_of_usage",
                    models.FloatField(blank=True, null=True),
                ),
            ],
            options={
                "db_table": "supplieritem",
                "managed": False,
            },
        ),
    ]
