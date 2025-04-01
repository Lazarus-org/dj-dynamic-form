from typing import Type

from rest_framework.serializers import BaseSerializer

from dynamic_form.api.serializers.user import UserSerializer
from dynamic_form.settings.conf import config


def dynamic_form_serializer_class(is_admin: bool = False) -> Type[BaseSerializer]:
    """Get the serializer class for the DynamicForm model, either from config
    or the default.

    Args:
        is_admin (bool): If True, returns the admin-specific serializer; otherwise, returns the regular serializer.
                         Defaults to False.

    Returns:
        The configured serializer class from settings or the default DynamicFormSerializer.

    """
    from dynamic_form.api.serializers.form import DynamicFormSerializer

    if is_admin:
        return config.api_admin_dynamic_form_serializer_class or DynamicFormSerializer
    return config.api_dynamic_form_serializer_class or DynamicFormSerializer


def dynamic_field_serializer_class(is_admin: bool = False) -> Type[BaseSerializer]:
    """Get the serializer class for the DynamicField model, either from config
    or the default.

    Args:
        is_admin (bool): If True, returns the admin-specific serializer; otherwise, returns the regular serializer.
                         Defaults to False.

    Returns:
        The configured serializer class from settings or the default DynamicFieldSerializer.

    """
    from dynamic_form.api.serializers.form import DynamicFieldSerializer

    if is_admin:
        return config.api_admin_dynamic_field_serializer_class or DynamicFieldSerializer
    return config.api_dynamic_field_serializer_class or DynamicFieldSerializer


def field_type_serializer_class(is_admin: bool = False) -> Type[BaseSerializer]:
    """Get the serializer class for the FieldType model, either from config or
    the default.

    Args:
        is_admin (bool): If True, returns the admin-specific serializer; otherwise, returns the regular serializer.
                         Defaults to False.

    Returns:
        The configured serializer class from settings or the default FieldTypeSerializer.

    """
    from dynamic_form.api.serializers.field_type import FieldTypeSerializer

    if is_admin:
        return config.api_admin_field_type_serializer_class or FieldTypeSerializer
    return config.api_field_type_serializer_class or FieldTypeSerializer


def form_submission_serializer_class(is_admin: bool = False) -> Type[BaseSerializer]:
    """Get the serializer class for the FormSubmission model, either from
    config or the default.

    Args:
        is_admin (bool): If True, returns the admin-specific serializer; otherwise, returns the regular serializer.
                         Defaults to False.

    Returns:
        The configured serializer class from settings or the default FormSubmissionSerializer.

    """
    from dynamic_form.api.serializers.form_submission import FormSubmissionSerializer

    if is_admin:
        return (
            config.api_admin_form_submission_serializer_class
            or FormSubmissionSerializer
        )
    return config.api_form_submission_serializer_class or FormSubmissionSerializer


def user_serializer_class() -> Type[BaseSerializer]:
    """Get the serializer class for the recipient and seen_by fields, either
    from config or the default."""
    return config.user_serializer_class or UserSerializer
