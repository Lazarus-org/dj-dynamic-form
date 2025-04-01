from rest_framework import serializers

from dynamic_form.models import FieldType


class FieldTypeSerializer(serializers.ModelSerializer):
    """Serializer for FieldType model."""

    class Meta:
        model = FieldType
        fields = "__all__"
