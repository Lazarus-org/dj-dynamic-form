from django.contrib import admin

from dynamic_form.mixins.admin.permission import AdminPermissionControlMixin
from dynamic_form.models import DynamicForm
from dynamic_form.settings.conf import config


@admin.register(DynamicForm, site=config.admin_site_class)
class DynamicFormAdmin(AdminPermissionControlMixin, admin.ModelAdmin):
    """
    Admin configuration for managing Dynamic Forms.
    """

    list_display = ("id", "name", "is_active", "created_at", "updated_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "description")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
