from django.db import models
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
    supplier_uuid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='supplier_uuid', blank=True, null=True)
    supplieritem_code = models.CharField(blank=True, null=True)
    supplieritem_description = models.CharField(blank=True, null=True)
    jitsuitem_uuid = models.ForeignKey(Jitsuitem, models.DO_NOTHING, db_column='jitsuitem_uuid', blank=True, null=True)
    unit_of_purchase = models.CharField(blank=True, null=True)
    quantity_unit_of_purchase_in_unit_of_usage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'supplieritem'
        unique_together = (('supplier_uuid', 'supplieritem_code'),)
