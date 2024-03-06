from django.db import models


class Jitsuitemcategory(models.Model):
    uuid = models.UUIDField(primary_key=True)
    deleted_row = models.BooleanField(blank=True, null=True)
    description = models.CharField()

    class Meta:
        managed = False
        db_table = 'jitsuitemcategory'

    def __str__(self):
        return self.description


# Create your models here.
class Jitsuitem(models.Model):
    uuid = models.UUIDField(primary_key=True)
    deleted_row = models.BooleanField(blank=True, null=True)
    description = models.CharField()
    category_uuid = models.ForeignKey(Jitsuitemcategory, models.DO_NOTHING, db_column='category_uuid', blank=True, null=True)
    unit_of_measure = models.CharField(blank=True, null=True)
    cost_per_unit_of_measure = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jitsuitem'

    def __str__(self):
        return self.description
