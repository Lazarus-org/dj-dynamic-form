from rest_framework import serializers

from dynamic_form.api.serializers.field import DynamicFieldSerializer
from dynamic_form.models import DynamicForm


class DynamicFormSerializer(serializers.ModelSerializer):
    """Serializer for DynamicForm model."""

    fields = DynamicFieldSerializer(many=True, read_only=True)

    class Meta:
        model = DynamicForm
        fields = "__all__"
