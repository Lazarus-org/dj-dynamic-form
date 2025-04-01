from typing import Any, List

from django.core.checks import Error, register

from dynamic_form.settings.conf import config
from dynamic_form.validators.config_validators import (
    validate_boolean_setting,
    validate_list_fields,
    validate_optional_path_setting,
    validate_optional_paths_setting,
    validate_throttle_rate,
)


@register()
def check_dynamic_form_settings(app_configs: Any, **kwargs: Any) -> List[Error]:
    """Check and validate DynamicForm-related settings in the Django
    configuration.

    This function performs validation of all DynamicForm-related settings defined in
    the Django settings, including admin settings, global API settings, and specific
    settings for DynamicForm, DynamicField, FieldType, FormSubmission, and their admin
    variants. It returns a list of errors if any issues are found.

    Parameters:
    -----------
    app_configs : Any
        Passed by Django during checks (not used here).

    kwargs : Any
        Additional keyword arguments for flexibility.

    Returns:
    --------
    List[Error]
        A list of `Error` objects for any detected configuration issues.

    """
    errors: List[Error] = []

    # Validate Admin settings (global)
    errors.extend(
        validate_boolean_setting(
            config.admin_has_add_permission, f"{config.prefix}ADMIN_HAS_ADD_PERMISSION"
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.admin_has_change_permission,
            f"{config.prefix}ADMIN_HAS_CHANGE_PERMISSION",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.admin_has_delete_permission,
            f"{config.prefix}ADMIN_HAS_DELETE_PERMISSION",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.admin_has_module_permission,
            f"{config.prefix}ADMIN_HAS_MODULE_PERMISSION",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(f"{config.prefix}ADMIN_SITE_CLASS", None),
            f"{config.prefix}ADMIN_SITE_CLASS",
        )
    )

    # Validate Global API settings
    errors.extend(
        validate_throttle_rate(
            config.base_user_throttle_rate, f"{config.prefix}BASE_USER_THROTTLE_RATE"
        )
    )
    errors.extend(
        validate_throttle_rate(
            config.staff_user_throttle_rate, f"{config.prefix}STAFF_USER_THROTTLE_RATE"
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(f"{config.prefix}API_ADMIN_PERMISSION_CLASS", None),
            f"{config.prefix}API_ADMIN_PERMISSION_CLASS",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(f"{config.prefix}API_USER_SERIALIZER_CLASS", None),
            f"{config.prefix}API_USER_SERIALIZER_CLASS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.user_serializer_fields, f"{config.prefix}API_USER_SERIALIZER_FIELDS"
        )
    )

    # Validate DynamicForm-specific API settings
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FORM_SERIALIZER_CLASS", None
            ),
            f"{config.prefix}API_DYNAMIC_FORM_SERIALIZER_CLASS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_dynamic_form_ordering_fields,
            f"{config.prefix}API_DYNAMIC_FORM_ORDERING_FIELDS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_dynamic_form_search_fields,
            f"{config.prefix}API_DYNAMIC_FORM_SEARCH_FIELDS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FORM_THROTTLE_CLASSES", None
            ),
            f"{config.prefix}API_DYNAMIC_FORM_THROTTLE_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FORM_PAGINATION_CLASS", None
            ),
            f"{config.prefix}API_DYNAMIC_FORM_PAGINATION_CLASS",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS", None
            ),
            f"{config.prefix}API_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(f"{config.prefix}API_DYNAMIC_FORM_PARSER_CLASSES", None),
            f"{config.prefix}API_DYNAMIC_FORM_PARSER_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FORM_FILTERSET_CLASS", None
            ),
            f"{config.prefix}API_DYNAMIC_FORM_FILTERSET_CLASS",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_dynamic_form_allow_list,
            f"{config.prefix}API_DYNAMIC_FORM_ALLOW_LIST",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_dynamic_form_allow_retrieve,
            f"{config.prefix}API_DYNAMIC_FORM_ALLOW_RETRIEVE",
        )
    )

    # Validate AdminDynamicForm-specific API settings
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FORM_SERIALIZER_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_SERIALIZER_CLASS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_admin_dynamic_form_ordering_fields,
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_ORDERING_FIELDS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_admin_dynamic_form_search_fields,
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_SEARCH_FIELDS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FORM_THROTTLE_CLASSES", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_THROTTLE_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FORM_PAGINATION_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_PAGINATION_CLASS",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FORM_PARSER_CLASSES", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_PARSER_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FORM_FILTERSET_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_FILTERSET_CLASS",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_dynamic_form_allow_list,
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_LIST",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_dynamic_form_allow_retrieve,
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_RETRIEVE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_dynamic_form_allow_create,
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_CREATE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_dynamic_form_allow_update,
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_UPDATE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_dynamic_form_allow_delete,
            f"{config.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_DELETE",
        )
    )

    # Validate DynamicField-specific API settings
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FIELD_SERIALIZER_CLASS", None
            ),
            f"{config.prefix}API_DYNAMIC_FIELD_SERIALIZER_CLASS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_dynamic_field_ordering_fields,
            f"{config.prefix}API_DYNAMIC_FIELD_ORDERING_FIELDS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_dynamic_field_search_fields,
            f"{config.prefix}API_DYNAMIC_FIELD_SEARCH_FIELDS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FIELD_THROTTLE_CLASSES", None
            ),
            f"{config.prefix}API_DYNAMIC_FIELD_THROTTLE_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FIELD_PAGINATION_CLASS", None
            ),
            f"{config.prefix}API_DYNAMIC_FIELD_PAGINATION_CLASS",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS", None
            ),
            f"{config.prefix}API_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FIELD_PARSER_CLASSES", None
            ),
            f"{config.prefix}API_DYNAMIC_FIELD_PARSER_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_DYNAMIC_FIELD_FILTERSET_CLASS", None
            ),
            f"{config.prefix}API_DYNAMIC_FIELD_FILTERSET_CLASS",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_dynamic_field_allow_list,
            f"{config.prefix}API_DYNAMIC_FIELD_ALLOW_LIST",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_dynamic_field_allow_retrieve,
            f"{config.prefix}API_DYNAMIC_FIELD_ALLOW_RETRIEVE",
        )
    )

    # Validate AdminDynamicField-specific API settings
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_SERIALIZER_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_SERIALIZER_CLASS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_admin_dynamic_field_ordering_fields,
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_ORDERING_FIELDS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_admin_dynamic_field_search_fields,
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_SEARCH_FIELDS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_THROTTLE_CLASSES", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_THROTTLE_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_PAGINATION_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_PAGINATION_CLASS",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_PARSER_CLASSES", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_PARSER_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_FILTERSET_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_FILTERSET_CLASS",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_dynamic_field_allow_list,
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_LIST",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_dynamic_field_allow_retrieve,
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_RETRIEVE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_dynamic_field_allow_create,
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_CREATE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_dynamic_field_allow_update,
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_UPDATE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_dynamic_field_allow_delete,
            f"{config.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_DELETE",
        )
    )

    # Validate FieldType-specific API settings
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(f"{config.prefix}API_FIELD_TYPE_SERIALIZER_CLASS", None),
            f"{config.prefix}API_FIELD_TYPE_SERIALIZER_CLASS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_field_type_ordering_fields,
            f"{config.prefix}API_FIELD_TYPE_ORDERING_FIELDS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_field_type_search_fields,
            f"{config.prefix}API_FIELD_TYPE_SEARCH_FIELDS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(f"{config.prefix}API_FIELD_TYPE_THROTTLE_CLASSES", None),
            f"{config.prefix}API_FIELD_TYPE_THROTTLE_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(f"{config.prefix}API_FIELD_TYPE_PAGINATION_CLASS", None),
            f"{config.prefix}API_FIELD_TYPE_PAGINATION_CLASS",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_FIELD_TYPE_EXTRA_PERMISSION_CLASS", None
            ),
            f"{config.prefix}API_FIELD_TYPE_EXTRA_PERMISSION_CLASS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(f"{config.prefix}API_FIELD_TYPE_PARSER_CLASSES", None),
            f"{config.prefix}API_FIELD_TYPE_PARSER_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(f"{config.prefix}API_FIELD_TYPE_FILTERSET_CLASS", None),
            f"{config.prefix}API_FIELD_TYPE_FILTERSET_CLASS",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_field_type_allow_list,
            f"{config.prefix}API_FIELD_TYPE_ALLOW_LIST",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_field_type_allow_retrieve,
            f"{config.prefix}API_FIELD_TYPE_ALLOW_RETRIEVE",
        )
    )

    # Validate AdminFieldType-specific API settings
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FIELD_TYPE_SERIALIZER_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_FIELD_TYPE_SERIALIZER_CLASS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_admin_field_type_ordering_fields,
            f"{config.prefix}API_ADMIN_FIELD_TYPE_ORDERING_FIELDS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_admin_field_type_search_fields,
            f"{config.prefix}API_ADMIN_FIELD_TYPE_SEARCH_FIELDS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FIELD_TYPE_THROTTLE_CLASSES", None
            ),
            f"{config.prefix}API_ADMIN_FIELD_TYPE_THROTTLE_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FIELD_TYPE_PAGINATION_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_FIELD_TYPE_PAGINATION_CLASS",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FIELD_TYPE_EXTRA_PERMISSION_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_FIELD_TYPE_EXTRA_PERMISSION_CLASS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FIELD_TYPE_PARSER_CLASSES", None
            ),
            f"{config.prefix}API_ADMIN_FIELD_TYPE_PARSER_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FIELD_TYPE_FILTERSET_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_FIELD_TYPE_FILTERSET_CLASS",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_field_type_allow_list,
            f"{config.prefix}API_ADMIN_FIELD_TYPE_ALLOW_LIST",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_field_type_allow_retrieve,
            f"{config.prefix}API_ADMIN_FIELD_TYPE_ALLOW_RETRIEVE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_field_type_allow_create,
            f"{config.prefix}API_ADMIN_FIELD_TYPE_ALLOW_CREATE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_field_type_allow_update,
            f"{config.prefix}API_ADMIN_FIELD_TYPE_ALLOW_UPDATE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_field_type_allow_delete,
            f"{config.prefix}API_ADMIN_FIELD_TYPE_ALLOW_DELETE",
        )
    )

    # Validate FormSubmission-specific API settings
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_FORM_SUBMISSION_SERIALIZER_CLASS", None
            ),
            f"{config.prefix}API_FORM_SUBMISSION_SERIALIZER_CLASS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_form_submission_ordering_fields,
            f"{config.prefix}API_FORM_SUBMISSION_ORDERING_FIELDS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_form_submission_search_fields,
            f"{config.prefix}API_FORM_SUBMISSION_SEARCH_FIELDS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_FORM_SUBMISSION_THROTTLE_CLASSES", None
            ),
            f"{config.prefix}API_FORM_SUBMISSION_THROTTLE_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_FORM_SUBMISSION_PAGINATION_CLASS", None
            ),
            f"{config.prefix}API_FORM_SUBMISSION_PAGINATION_CLASS",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS", None
            ),
            f"{config.prefix}API_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_FORM_SUBMISSION_PARSER_CLASSES", None
            ),
            f"{config.prefix}API_FORM_SUBMISSION_PARSER_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_FORM_SUBMISSION_FILTERSET_CLASS", None
            ),
            f"{config.prefix}API_FORM_SUBMISSION_FILTERSET_CLASS",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_form_submission_allow_list,
            f"{config.prefix}API_FORM_SUBMISSION_ALLOW_LIST",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_form_submission_allow_retrieve,
            f"{config.prefix}API_FORM_SUBMISSION_ALLOW_RETRIEVE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_form_submission_allow_create,
            f"{config.prefix}API_FORM_SUBMISSION_ALLOW_CREATE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_form_submission_allow_update,
            f"{config.prefix}API_FORM_SUBMISSION_ALLOW_UPDATE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_form_submission_allow_delete,
            f"{config.prefix}API_FORM_SUBMISSION_ALLOW_DELETE",
        )
    )

    # Validate AdminFormSubmission-specific API settings
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FORM_SUBMISSION_SERIALIZER_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_SERIALIZER_CLASS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_admin_form_submission_ordering_fields,
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_ORDERING_FIELDS",
        )
    )
    errors.extend(
        validate_list_fields(
            config.api_admin_form_submission_search_fields,
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_SEARCH_FIELDS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FORM_SUBMISSION_THROTTLE_CLASSES", None
            ),
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_THROTTLE_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FORM_SUBMISSION_PAGINATION_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_PAGINATION_CLASS",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS",
        )
    )
    errors.extend(
        validate_optional_paths_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FORM_SUBMISSION_PARSER_CLASSES", None
            ),
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_PARSER_CLASSES",
        )
    )
    errors.extend(
        validate_optional_path_setting(
            config.get_setting(
                f"{config.prefix}API_ADMIN_FORM_SUBMISSION_FILTERSET_CLASS", None
            ),
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_FILTERSET_CLASS",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_form_submission_allow_list,
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_LIST",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_form_submission_allow_retrieve,
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_RETRIEVE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_form_submission_allow_create,
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_CREATE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_form_submission_allow_update,
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_UPDATE",
        )
    )
    errors.extend(
        validate_boolean_setting(
            config.api_admin_form_submission_allow_delete,
            f"{config.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_DELETE",
        )
    )

    return errors
