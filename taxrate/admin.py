from django.contrib import admin

# Register your models here.
from .models import TaxRate


class TaxRateAdmin(admin.ModelAdmin):
    list_display = (
        'tax_name',
        'display_tax_rate_percentage',
        'date_begin',
        )

    def display_tax_rate_percentage(self, obj):
        return f'{obj.tax_rate * 100:.2f}%'

    display_tax_rate_percentage.short_description = 'Tax Rate (%)'


admin.site.register(TaxRate, TaxRateAdmin)
