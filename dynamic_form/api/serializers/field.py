from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from dynamic_form.api.serializers.field_type import FieldTypeSerializer
from dynamic_form.models import DynamicField, DynamicForm, FieldType


class DynamicFieldSerializer(serializers.ModelSerializer):
    """Serializer for DynamicField model.

    Validates that each field name is unique within its associated form
    during creation and updates. Ensures the referenced form exists and
    is active. Supports partial updates (PATCH) by making field_type_id
    optional.

    """

    field_type = FieldTypeSerializer(read_only=True)
    field_type_id = serializers.IntegerField(
        write_only=True,
        label=_("Field Type ID"),
        help_text=_("The ID of the Field Type related to this Field."),
    )

    class Meta:
        model = DynamicField
        fields = "__all__"
        read_only_fields = ["form"]

    def validate(self, attrs):
        """Validate the field data, ensuring the field type exists and the
        field name is unique per form.

        For PATCH updates, only validates field_type_id if provided.
        Preserves existing form and field_type if not included in the request.

        Args:
            attrs (dict): The incoming data to validate.

        Returns:
            dict: The validated attributes with the resolved form instance.

        Raises:
            serializers.ValidationError: If the form is invalid or the field name is not unique.

        """
        # Get form from view's URL kwargs
        view = self.context.get("view")
        form_pk = view.kwargs.get("form_pk") if view else None

        if not form_pk or not str(form_pk).isdigit():
            raise serializers.ValidationError(
                {"form_pk": _("Invalid Form ID specified in the URL.")}
            )

        if not (self.instance and self.instance.form_id):
            form = DynamicForm.objects.filter(is_active=True, pk=form_pk).first()
            if not form:
                raise serializers.ValidationError(
                    {"form": _("Specified form not found or inactive.")}
                )
        else:
            form = self.instance.form

        attrs["form"] = form
        # Handle field_type_id if provided
        field_type_id = attrs.pop("field_type_id", None)
        if field_type_id is not None:
            field_type = FieldType.objects.filter(pk=field_type_id).first()
            if not field_type:
                raise serializers.ValidationError(
                    {"field_type_id": _("Field Type with the given ID was not found.")}
                )
            attrs["field_type"] = field_type
        else:
            # Use the existing field_type for updates if field_type_id is not provided
            attrs["field_type"] = self.instance.field_type

        # Extract the name from the incoming data (if provided)
        name = attrs.get("name")
        if name is not None:
            instance = self.instance  # None for create, existing instance for update
            conflicting_field = (
                DynamicField.objects.filter(form=attrs["form"], name=name)
                .exclude(
                    pk=(
                        instance.pk if instance else None
                    )  # Exclude current instance during update
                )
                .exists()
            )
            if conflicting_field:
                raise serializers.ValidationError(
                    {
                        "name": _(
                            "A field with this name already exists in the specified form."
                        )
                    }
                )

        return attrs
