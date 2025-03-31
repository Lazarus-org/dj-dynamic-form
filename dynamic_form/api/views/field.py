from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from dynamic_form.api.serializers.helper.get_serializer_cls import (
    dynamic_field_serializer_class,
)
from dynamic_form.api.views.base import BaseViewSet, AdminViewSet
from dynamic_form.models import DynamicField


class AdminDynamicFieldViewSet(AdminViewSet, ModelViewSet):
    """
    API for managing Dynamic Fields inside a form.
    """

    config_prefix = "admin_dynamic_field"
    queryset = DynamicField.objects.select_related("field_type").all()
    serializer_class = dynamic_field_serializer_class(is_admin=True)


class DynamicFieldViewSet(BaseViewSet, ListModelMixin, RetrieveModelMixin):
    """
    API for managing Dynamic Fields inside a form.
    """

    config_prefix = "dynamic_field"
    queryset = DynamicField.objects.select_related("field_type").all()
    serializer_class = dynamic_field_serializer_class()
