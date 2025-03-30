from rest_framework.routers import DefaultRouter
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
router.register(r"admin/fields", AdminDynamicFieldViewSet, basename="admin-field")
router.register(
    r"admin/field-types", AdminFieldTypeViewSet, basename="admin-field-type"
)
router.register(
    r"admin/submissions", AdminFormSubmissionViewSet, basename="admin-form-submission"
)

urlpatterns = router.urls
