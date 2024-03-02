from django.contrib import admin

# Register your models here.
from .models import Jitsuitem, Jitsuitemcategory


class JitsuitemAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'get_category_description',
        'unit_of_measure',
        'cost_per_unit_of_measure',
        )

    list_filter = ('category_uuid__description',)
    list_per_page = 20
    ordering = ('description',)

    def get_category_description(self, obj):
        if obj.category_uuid:
            return obj.category_uuid.description
        return None

    get_category_description.short_description = 'Category'


admin.site.register(Jitsuitem, JitsuitemAdmin)


class JitsuitemcategoryAdmin(admin.ModelAdmin):
    list_display = ('description',)
    ordering = ('description',)


admin.site.register(Jitsuitemcategory, JitsuitemcategoryAdmin)
