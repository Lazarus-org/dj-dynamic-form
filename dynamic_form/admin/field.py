from django.contrib import admin

from dynamic_form.mixins.admin.permission import AdminPermissionControlMixin
from dynamic_form.models import DynamicField
from dynamic_form.settings.conf import config


@admin.register(DynamicField, site=config.admin_site_class)
class DynamicFieldAdmin(AdminPermissionControlMixin, admin.ModelAdmin):
    """
    Admin configuration for managing Dynamic Fields within Forms.
    """

    list_display = ("id", "name", "form", "field_type", "is_required", "order")
    list_display_links = ("id", "name")
    autocomplete_fields = ("form", "field_type")
    list_filter = ("field_type", "is_required", "form")
    search_fields = ("name", "form__name")
    ordering = ("order", "name")
