from django.contrib import admin

from dynamic_form.mixins.admin.permission import AdminPermissionControlMixin
from dynamic_form.models import FormSubmission
from dynamic_form.settings.conf import config


@admin.register(FormSubmission, site=config.admin_site_class)
class FormSubmissionAdmin(AdminPermissionControlMixin, admin.ModelAdmin):
    """
    Admin configuration for managing Form Submissions.
    """

    list_display = ("id", "user", "form", "submitted_at")
    list_display_links = ("id", "user")
    list_select_related = ("user", "form")
    list_filter = ("submitted_at", "form")
    search_fields = ("form__name",)
    ordering = ("-submitted_at",)
    readonly_fields = ("user", "submitted_at", "submitted_data")

    def has_add_permission(self, request, obj=...):
        return False

    def has_change_permission(self, request, obj=...):
        return False
