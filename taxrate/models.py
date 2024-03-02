from django.db import models


# Create your models here.
class TaxRate(models.Model):
    uuid = models.UUIDField(primary_key=True)
    date_begin = models.DateField(db_comment='starting date of tax')
    date_end = models.DateField(blank=True, null=True, db_comment='ending date of tax')
    tax_name = models.CharField(max_length=20)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_rate'

    def __str__(self):
        return f"{self.tax_name} - {self.tax_rate * 100} % - From: {self.date_begin} to: {self.date_end}"
