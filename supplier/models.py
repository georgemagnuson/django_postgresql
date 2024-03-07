from django.db import models
from django.db.models import UniqueConstraint
from jitsuitem.models import Jitsuitem


# Create your models here.
class Supplier(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(unique=True, blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    includes_gst_in_prices = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'

    def __str__(self):
        return self.name


class Supplieritem(models.Model):
    uuid = models.UUIDField(primary_key=True)
    deleted_row = models.BooleanField(blank=True, null=True)
    supplier_uuid = models.ForeignKey(
        Supplier,
        models.DO_NOTHING,
        db_column='supplier_uuid',
        blank=True,
        null=True)
    supplieritem_code = models.CharField(db_column='supplieritem_code', blank=True, null=True)
    supplieritem_description = models.CharField(blank=True, null=True)
    jitsuitem_uuid = models.ForeignKey(
        Jitsuitem,
        to_field='uuid',
        on_delete=models.DO_NOTHING,
        db_column='jitsuitem_uuid',
        blank=True,
        null=True
        )
    unit_of_purchase = models.CharField(blank=True, null=True)
    quantity_unit_of_purchase_in_unit_of_usage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplieritem'
        unique_together = (('supplier_uuid', 'supplieritem_code'),)
        constraints = [
            UniqueConstraint(fields=['jitsuitem_uuid'], name='unique_jitsuitem_uuid')
            ]

    def __str__(self):
        return f'{self.supplieritem_code} - {self.supplieritem_description}'


class Message(models.Model):
    uuid = models.UUIDField(primary_key=True)
    gmail_message_id = models.CharField(unique=True, blank=True, null=True)
    message_date = models.DateField(blank=True, null=True)
    message_from = models.CharField(blank=True, null=True)
    message_to = models.CharField(blank=True, null=True)
    message_subject = models.CharField(blank=True, null=True)
    message_raw = models.CharField(blank=True, null=True)
    deleted_row = models.BooleanField(blank=True, null=True, db_comment='instead of deleting just check this')
    message_has_attachments = models.BooleanField(blank=True, null=True)
    message_processed = models.BooleanField(blank=True, null=True)
    message_status = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'

    def __str__(self):
        return f'{self.message_date} - From:{self.message_from} - Subject:{self.message_subject}'


class Invoice(models.Model):
    uuid = models.UUIDField(primary_key=True)
    gmail_message = models.ForeignKey(
        Message,
        models.DO_NOTHING,
        to_field='gmail_message_id',
        blank=True,
        null=True
        )

    invoice_date = models.DateField()
    invoice_issuer = models.ForeignKey(
        Supplier,
        models.DO_NOTHING,
        db_column='invoice_issuer',
        to_field='name',
        blank=True,
        null=True
        )

    invoice_supplier_uuid = models.UUIDField(blank=True, null=True)

    invoice_number = models.CharField()
    invoice_amount_gross = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    invoice_amount_gst = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    invoice_amount_net = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    invoice_credit = models.BooleanField(blank=True, null=True)
    deleted_row = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'

    def __str__(self):
        return f'{self.invoice_issuer} - {self.invoice_date} - {self.invoice_number}'


class Invoiceentry(models.Model):
    uuid = models.UUIDField(primary_key=True)
    invoice_uuid = models.ForeignKey(
        Invoice,
        db_column='invoice_uuid',
        to_field='uuid',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
        )

    entry_supplieritem_code = models.CharField(blank=True, null=True)
    entry_supplieritem_description = models.CharField(blank=True, null=True)

    entry_qty = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    entry_unit_of_purchase = models.CharField(blank=True, null=True)
    entry_price = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    entry_discount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    entry_gross_weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    entry_net_weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    entry_number_of_pieces = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    entry_waste_weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    supplier_uuid = models.UUIDField(db_column='supplier_uuid', blank=True, null=True)
    supplieritem_uuid = models.UUIDField(db_column='supplieritem_uuid', blank=True, null=True)

    entry_jitsuitem_uuid = models.ForeignKey(
        Supplieritem,
        to_field='jitsuitem_uuid',
        on_delete=models.DO_NOTHING,
        db_column='entry_jitsuitem_uuid',
        blank=True,
        null=True
        )

    deleted_row = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoiceentry'

    def __str__(self):
        return f'{self.entry_supplieritem_code} : {self.entry_supplieritem_description} - {self.entry_qty}'


