from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html

from .models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("preview", "title", "is_active", "order")
    list_editable = ("is_active",)
    search_fields = ("title",)
    list_filter = ("is_active",)
    ordering = ("order",)
    fieldsets = (
        (None, {"fields": ("title", "image", "is_active")}),
        ("Сортировка", {"fields": ("order",)}),
    )

    def preview(self, obj: SliderImage) -> str:
        if obj.image_id and obj.image:
            return format_html(
                '<img src="{}" width="100" style="object-fit: cover;" />',
                obj.image.url,
            )
        return "-"

    preview.short_description = "Превью"

