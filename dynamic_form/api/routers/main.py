from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from dynamic_form.api.views import (
    DynamicFormViewSet,
    DynamicFieldViewSet,
    FieldTypeViewSet,
    FormSubmissionViewSet,
    AdminDynamicFormViewSet,
    AdminDynamicFieldViewSet,
    AdminFieldTypeViewSet,
    AdminFormSubmissionViewSet,
)

router = DefaultRouter()

# Regular user-facing endpoints
router.register(r"forms", DynamicFormViewSet, basename="form")
router.register(r"fields", DynamicFieldViewSet, basename="field")
router.register(r"field-types", FieldTypeViewSet, basename="field-type")
router.register(r"submissions", FormSubmissionViewSet, basename="form-submission")

# Admin endpoints
router.register(r"admin/forms", AdminDynamicFormViewSet, basename="admin-form")
router.register(
    r"admin/field-types", AdminFieldTypeViewSet, basename="admin-field-type"
)
router.register(
    r"admin/submissions", AdminFormSubmissionViewSet, basename="admin-form-submission"
)

# Nested router for fields under forms
admin_form_router = NestedDefaultRouter(router, r"admin/forms", lookup="form")
admin_form_router.register(
    r"fields", AdminDynamicFieldViewSet, basename="admin-form-field"
)

urlpatterns = router.urls + admin_form_router.urls
