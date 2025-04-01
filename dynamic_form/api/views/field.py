from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet

from dynamic_form.api.serializers.helper.get_serializer_cls import (
    dynamic_field_serializer_class,
)
from dynamic_form.api.views.base import AdminViewSet, BaseViewSet
from dynamic_form.models import DynamicField


class AdminDynamicFieldViewSet(AdminViewSet, ModelViewSet):
    """API for managing Dynamic Fields inside a form."""

    config_prefix = "admin_dynamic_field"
    serializer_class = dynamic_field_serializer_class(is_admin=True)

    def get_queryset(self):
        """Filter the queryset to only include fields for the specified form_pk
        from the URL.

        Returns:
            Queryset of DynamicField objects filtered by form_pk.

        """
        form_pk = self.kwargs.get("form_pk")
        if not str(form_pk).isdigit():
            raise ValidationError(
                {
                    "form_pk": _(
                        "Invalid form identifier '%(form_pk)s'. The ID must be a numeric value."
                    )
                    % {"form_pk": form_pk}
                },
                code="invalid_form_id",
            )

        return DynamicField.objects.select_related("field_type").filter(form_id=form_pk)


class DynamicFieldViewSet(BaseViewSet, ListModelMixin, RetrieveModelMixin):
    """API for managing Dynamic Fields inside a form."""

    config_prefix = "dynamic_field"
    queryset = DynamicField.objects.select_related("field_type").all()
    serializer_class = dynamic_field_serializer_class()
