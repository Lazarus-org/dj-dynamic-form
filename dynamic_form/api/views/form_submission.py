from rest_framework.viewsets import ModelViewSet

from dynamic_form.api.serializers.helper.get_serializer_cls import (
    form_submission_serializer_class,
)
from dynamic_form.api.views.base import AdminViewSet, BaseViewSet
from dynamic_form.models import FormSubmission


class AdminFormSubmissionViewSet(AdminViewSet, ModelViewSet):
    """API for managing form submissions."""

    config_prefix = "admin_form_submission"
    queryset = (
        FormSubmission.objects.select_related("user", "form")
        .prefetch_related("form__fields__field_type")
        .all()
    )
    serializer_class = form_submission_serializer_class(is_admin=True)


class FormSubmissionViewSet(BaseViewSet, ModelViewSet):
    """API for managing form submissions."""

    config_prefix = "form_submission"
    serializer_class = form_submission_serializer_class()

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated or not user.id:
            return FormSubmission.objects.none()

        return (
            FormSubmission.objects.select_related("user", "form")
            .prefetch_related("form__fields__field_type")
            .filter(user_id=user.id)
        )
