from django.contrib import admin
from django.db.models.functions import Upper
# Register your models here.
from .models import Supplier, Supplieritem


class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'includes_gst_in_prices',
        )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(upper_name=Upper('name')).order_by('upper_name')


admin.site.register(Supplier, SupplierAdmin)


class SupplieritemAdmin(admin.ModelAdmin):
    list_display = (
        'supplier_uuid',
        'supplieritem_code',
        'supplieritem_description',
        'jitsuitem_uuid_description',
        'unit_of_purchase',
        'qty_purch_in_usage',
        )

    list_per_page = 20

    def jitsuitem_uuid_description(self, obj):
        if obj.jitsuitem_uuid:
            return obj.jitsuitem_uuid.description
        return None

    jitsuitem_uuid_description.short_description = 'Jitsuitem Description'

    def qty_purch_in_usage(self, obj):
        return obj.quantity_unit_of_purchase_in_unit_of_usage

    qty_purch_in_usage.short_description = 'Qty Purch in Unit of Usage'
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(upper_supplieritem_code=Upper('supplieritem_code')).order_by(
            'upper_supplieritem_code'
            )


admin.site.register(Supplieritem, SupplieritemAdmin)
