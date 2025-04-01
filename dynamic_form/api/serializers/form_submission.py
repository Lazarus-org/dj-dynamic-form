from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from dynamic_form.api.serializers.form import DynamicFormSerializer
from dynamic_form.api.serializers.helper.get_serializer_cls import user_serializer_class
from dynamic_form.models import DynamicForm, FormSubmission


class FormSubmissionSerializer(serializers.ModelSerializer):
    """Serializer for FormSubmission model."""

    form = DynamicFormSerializer(read_only=True)
    form_id = serializers.IntegerField(
        write_only=True,
        label=_("Form ID"),
        help_text=_("The ID of the form to which this submission belongs."),
    )
    user = user_serializer_class()(read_only=True)

    class Meta:
        model = FormSubmission
        fields = "__all__"
        read_only_fields = ["submitted_at", "user"]

    def validate(self, attrs):
        """Validates that submitted data matches the expected form
        structure."""
        form_id = (
            attrs["form_id"]
            if attrs.get("form_id") is not None
            else self.instance.form_id if self.instance and self.partial else None
        )
        submitted_data = (
            attrs["submitted_data"]
            if attrs.get("submitted_data") is not None
            else (
                self.instance.submitted_data if self.instance and self.partial else None
            )
        )

        if not submitted_data:
            raise serializers.ValidationError(
                {"submitted_data": _("This field may not be null.")}
            )

        form = (
            DynamicForm.objects.prefetch_related("fields")
            .filter(is_active=True, pk=form_id)
            .first()
        )
        if not form:
            raise serializers.ValidationError(
                {"form_id": _("Form with the given ID was not found or is inactive.")}
            )
        all_fields = form.fields.all()
        for field in all_fields:
            if field.is_required and field.name not in submitted_data:
                raise serializers.ValidationError(
                    {field.name: _("This field is required.")}
                )

        return attrs

    def create(self, validated_data):
        """Create a new FormSubmission instance, setting the user from the
        request if authenticated."""
        request = self.context.get("request")
        if request and hasattr(request, "user") and request.user.is_authenticated:
            validated_data["user"] = request.user

        return super().create(validated_data)
