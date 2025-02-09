from rest_framework import serializers
from .models import DynamicForm, DynamicField, FormSubmission

class DynamicFieldSerializer(serializers.ModelSerializer):
    """
    Serializer for DynamicField model.
    """
    class Meta:
        model = DynamicField
        fields = "__all__"

class DynamicFormSerializer(serializers.ModelSerializer):
    """
    Serializer for DynamicForm model with nested DynamicField serialization.
    """
    fields = DynamicFieldSerializer(many=True)

    class Meta:
        model = DynamicForm
        fields = "__all__"

    def create(self, validated_data):
        """
        Custom create method to handle nested field data.
        """
        fields_data = validated_data.pop("fields", [])
        form = DynamicForm.objects.create(**validated_data)
        for field_data in fields_data:
            DynamicField.objects.create(form=form, **field_data)
        return form


class FormSubmissionSerializer(serializers.ModelSerializer):
    """
    Serializer for FormSubmission model.
    """

    class Meta:
        model = FormSubmission
        fields = "__all__"

    def validate(self, data):
        """
        Validates that submitted data matches the expected form structure.
        """
        form = data["form"]
        submitted_data = data["submitted_data"]

        for field in form.fields.all():
            if field.is_required and field.name not in submitted_data:
                raise serializers.ValidationError({field.name: "This field is required."})

            if field.field_type == "number" and not isinstance(submitted_data.get(field.name), (int, float)):
                raise serializers.ValidationError({field.name: "Must be a number."})

        return data
