from django.contrib import admin
from .models import DynamicForm, DynamicField, FormSubmission

@admin.register(DynamicForm)
class DynamicFormAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Dynamic Forms.
    """
    list_display = ("name", "description", "created_at")
    search_fields = ("name", "description")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

@admin.register(DynamicField)
class DynamicFieldAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Dynamic Fields within Forms.
    """
    list_display = ("name", "form", "field_type", "is_required")
    autocomplete_fields = ("form",)
    list_filter = ("field_type", "is_required", "form")
    search_fields = ("name", "form__name")
    ordering = ("form", "name")

@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Form Submissions.
    """
    list_display = ("form", "submitted_at")
    list_filter = ("submitted_at", "form")
    search_fields = ("form__name",)
    ordering = ("-submitted_at",)
    readonly_fields = ("submitted_at", "submitted_data")


    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False
    