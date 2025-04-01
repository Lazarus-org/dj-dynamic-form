from django.contrib import admin

from dynamic_form.mixins.admin.permission import AdminPermissionControlMixin
from dynamic_form.models import FieldType
from dynamic_form.settings.conf import config


@admin.register(FieldType, site=config.admin_site_class)
class FieldTypeAdmin(AdminPermissionControlMixin, admin.ModelAdmin):
    """Admin configuration for managing Field Types."""

    list_display = ("id", "name", "label", "is_active", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "description")
    list_filter = ("is_active", "created_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
