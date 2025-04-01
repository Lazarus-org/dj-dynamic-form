from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet

from dynamic_form.api.serializers.helper.get_serializer_cls import (
    field_type_serializer_class,
)
from dynamic_form.api.views.base import AdminViewSet, BaseViewSet
from dynamic_form.models import FieldType


class AdminFieldTypeViewSet(AdminViewSet, ModelViewSet):
    """API for managing Field Types inside a form."""

    config_prefix = "admin_field_type"
    queryset = FieldType.objects.all()
    serializer_class = field_type_serializer_class(is_admin=True)


class FieldTypeViewSet(BaseViewSet, ListModelMixin, RetrieveModelMixin):
    """API for managing Field Types inside a form."""

    config_prefix = "field_type"
    queryset = FieldType.objects.filter(is_active=True)
    serializer_class = field_type_serializer_class()
