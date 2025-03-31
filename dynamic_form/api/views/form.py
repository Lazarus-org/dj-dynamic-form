from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet

from dynamic_form.api.serializers.helper.get_serializer_cls import dynamic_form_serializer_class
from dynamic_form.api.views.base import BaseViewSet, AdminViewSet
from dynamic_form.models import DynamicForm


class AdminDynamicFormViewSet(AdminViewSet, ModelViewSet):
    """
    API for managing Dynamic Forms.
    """

    config_prefix = "admin_dynamic_form"
    queryset = DynamicForm.objects.prefetch_related("fields__field_type").all()
    serializer_class = dynamic_form_serializer_class(is_admin=True)


class DynamicFormViewSet(BaseViewSet, ListModelMixin, RetrieveModelMixin):
    """
    API for managing Dynamic Forms.
    """

    config_prefix = "dynamic_form"
    queryset = DynamicForm.objects.prefetch_related("fields__field_type").filter(
        is_active=True, fields__field_type__is_active=True
    )
    serializer_class = dynamic_form_serializer_class()
