from typing import Any, List, Optional

from django.conf import settings
from django.utils.module_loading import import_string

from dynamic_form.constants.default_settings import (
    admin_settings,
    api_dynamic_field_settings,
    api_dynamic_form_settings,
    api_field_type_settings,
    api_form_submission_settings,
    api_settings,
    serializer_settings,
    throttle_settings,
)
from dynamic_form.constants.types import DefaultPath, OptionalPaths


class DynamicFormConfig:
    """A configuration handler.

    Allows dynamic settings loading from Django settings with default
    fallbacks for all DynamicForm-related APIs, including DynamicForm,
    DynamicField, FieldType, FormSubmission, and their admin variants.

    """

    prefix = "DYNAMIC_FORM_"

    def __init__(self) -> None:
        # Admin settings (global)
        self.admin_has_add_permission: bool = self.get_setting(
            f"{self.prefix}ADMIN_HAS_ADD_PERMISSION",
            admin_settings.admin_has_add_permission,
        )
        self.admin_has_change_permission: bool = self.get_setting(
            f"{self.prefix}ADMIN_HAS_CHANGE_PERMISSION",
            admin_settings.admin_has_change_permission,
        )
        self.admin_has_delete_permission: bool = self.get_setting(
            f"{self.prefix}ADMIN_HAS_DELETE_PERMISSION",
            admin_settings.admin_has_delete_permission,
        )
        self.admin_has_module_permission: bool = self.get_setting(
            f"{self.prefix}ADMIN_HAS_MODULE_PERMISSION",
            admin_settings.admin_has_module_permission,
        )
        self.admin_site_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}ADMIN_SITE_CLASS",
            admin_settings.admin_site_class,
        )

        # Global API settings
        self.base_user_throttle_rate: str = self.get_setting(
            f"{self.prefix}BASE_USER_THROTTLE_RATE",
            throttle_settings.base_user_throttle_rate,
        )
        self.staff_user_throttle_rate: str = self.get_setting(
            f"{self.prefix}STAFF_USER_THROTTLE_RATE",
            throttle_settings.staff_user_throttle_rate,
        )
        self.api_admin_permission_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_ADMIN_PERMISSION_CLASS",
            api_settings.admin_permission_class,
        )
        self.user_serializer_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_USER_SERIALIZER_CLASS",
            serializer_settings.user_serializer_class,
        )
        self.user_serializer_fields: List[str] = self.get_setting(
            f"{self.prefix}API_USER_SERIALIZER_FIELDS",
            serializer_settings.user_serializer_fields,
        )

        # DynamicForm-specific API settings
        self.api_dynamic_form_serializer_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_DYNAMIC_FORM_SERIALIZER_CLASS",
            serializer_settings.dynamic_form_serializer_class,
        )
        self.api_dynamic_form_ordering_fields: List[str] = self.get_setting(
            f"{self.prefix}API_DYNAMIC_FORM_ORDERING_FIELDS",
            api_dynamic_form_settings.ordering_fields,
        )
        self.api_dynamic_form_search_fields: List[str] = self.get_setting(
            f"{self.prefix}API_DYNAMIC_FORM_SEARCH_FIELDS",
            api_dynamic_form_settings.search_fields,
        )
        self.api_dynamic_form_throttle_classes: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_DYNAMIC_FORM_THROTTLE_CLASSES",
            throttle_settings.throttle_class,
        )
        self.api_dynamic_form_pagination_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_DYNAMIC_FORM_PAGINATION_CLASS",
            api_settings.pagination_class,
        )
        self.api_dynamic_form_extra_permission_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS",
                api_settings.extra_permission_class,
            )
        )
        self.api_dynamic_form_parser_classes: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_DYNAMIC_FORM_PARSER_CLASSES",
            api_settings.parser_classes,
        )
        self.api_dynamic_form_filterset_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_DYNAMIC_FORM_FILTERSET_CLASS",
            api_dynamic_form_settings.filterset_class,
        )
        self.api_dynamic_form_allow_list: bool = self.get_setting(
            f"{self.prefix}API_DYNAMIC_FORM_ALLOW_LIST",
            api_dynamic_form_settings.allow_list,
        )
        self.api_dynamic_form_allow_retrieve: bool = self.get_setting(
            f"{self.prefix}API_DYNAMIC_FORM_ALLOW_RETRIEVE",
            api_dynamic_form_settings.allow_retrieve,
        )

        # AdminDynamicForm-specific API settings
        self.api_admin_dynamic_form_serializer_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FORM_SERIALIZER_CLASS",
                serializer_settings.dynamic_form_serializer_class,
            )
        )
        self.api_admin_dynamic_form_ordering_fields: List[str] = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FORM_ORDERING_FIELDS",
            api_dynamic_form_settings.ordering_fields,
        )
        self.api_admin_dynamic_form_search_fields: List[str] = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FORM_SEARCH_FIELDS",
            api_dynamic_form_settings.search_fields,
        )
        self.api_admin_dynamic_form_throttle_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FORM_THROTTLE_CLASSES",
                throttle_settings.throttle_class,
            )
        )
        self.api_admin_dynamic_form_pagination_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FORM_PAGINATION_CLASS",
                api_settings.pagination_class,
            )
        )
        self.api_admin_dynamic_form_extra_permission_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS",
                api_settings.extra_permission_class,
            )
        )
        self.api_admin_dynamic_form_parser_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FORM_PARSER_CLASSES",
                api_settings.parser_classes,
            )
        )
        self.api_admin_dynamic_form_filterset_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FORM_FILTERSET_CLASS",
                api_dynamic_form_settings.filterset_class,
            )
        )
        self.api_admin_dynamic_form_allow_list: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_LIST",
            api_dynamic_form_settings.admin_allow_list,
        )
        self.api_admin_dynamic_form_allow_retrieve: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_RETRIEVE",
            api_dynamic_form_settings.admin_allow_retrieve,
        )
        self.api_admin_dynamic_form_allow_create: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_CREATE",
            api_dynamic_form_settings.admin_allow_create,
        )
        self.api_admin_dynamic_form_allow_update: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_UPDATE",
            api_dynamic_form_settings.admin_allow_update,
        )
        self.api_admin_dynamic_form_allow_delete: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_DELETE",
            api_dynamic_form_settings.admin_allow_delete,
        )

        # DynamicField-specific API settings
        self.api_dynamic_field_serializer_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_DYNAMIC_FIELD_SERIALIZER_CLASS",
                serializer_settings.dynamic_field_serializer_class,
            )
        )
        self.api_dynamic_field_ordering_fields: List[str] = self.get_setting(
            f"{self.prefix}API_DYNAMIC_FIELD_ORDERING_FIELDS",
            api_dynamic_field_settings.ordering_fields,
        )
        self.api_dynamic_field_search_fields: List[str] = self.get_setting(
            f"{self.prefix}API_DYNAMIC_FIELD_SEARCH_FIELDS",
            api_dynamic_field_settings.search_fields,
        )
        self.api_dynamic_field_throttle_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_DYNAMIC_FIELD_THROTTLE_CLASSES",
                throttle_settings.throttle_class,
            )
        )
        self.api_dynamic_field_pagination_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_DYNAMIC_FIELD_PAGINATION_CLASS",
                api_settings.pagination_class,
            )
        )
        self.api_dynamic_field_extra_permission_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS",
                api_settings.extra_permission_class,
            )
        )
        self.api_dynamic_field_parser_classes: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_DYNAMIC_FIELD_PARSER_CLASSES",
            api_settings.parser_classes,
        )
        self.api_dynamic_field_filterset_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_DYNAMIC_FIELD_FILTERSET_CLASS",
            api_dynamic_field_settings.filterset_class,
        )
        self.api_dynamic_field_allow_list: bool = self.get_setting(
            f"{self.prefix}API_DYNAMIC_FIELD_ALLOW_LIST",
            api_dynamic_field_settings.allow_list,
        )
        self.api_dynamic_field_allow_retrieve: bool = self.get_setting(
            f"{self.prefix}API_DYNAMIC_FIELD_ALLOW_RETRIEVE",
            api_dynamic_field_settings.allow_retrieve,
        )

        # AdminDynamicField-specific API settings
        self.api_admin_dynamic_field_serializer_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_SERIALIZER_CLASS",
                serializer_settings.dynamic_field_serializer_class,
            )
        )
        self.api_admin_dynamic_field_ordering_fields: List[str] = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_ORDERING_FIELDS",
            api_dynamic_field_settings.ordering_fields,
        )
        self.api_admin_dynamic_field_search_fields: List[str] = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_SEARCH_FIELDS",
            api_dynamic_field_settings.search_fields,
        )
        self.api_admin_dynamic_field_throttle_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_THROTTLE_CLASSES",
                throttle_settings.throttle_class,
            )
        )
        self.api_admin_dynamic_field_pagination_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_PAGINATION_CLASS",
                api_settings.pagination_class,
            )
        )
        self.api_admin_dynamic_field_extra_permission_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS",
                api_settings.extra_permission_class,
            )
        )
        self.api_admin_dynamic_field_parser_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_PARSER_CLASSES",
                api_settings.parser_classes,
            )
        )
        self.api_admin_dynamic_field_filterset_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_FILTERSET_CLASS",
                api_dynamic_field_settings.filterset_class,
            )
        )
        self.api_admin_dynamic_field_allow_list: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_LIST",
            api_dynamic_field_settings.admin_allow_list,
        )
        self.api_admin_dynamic_field_allow_retrieve: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_RETRIEVE",
            api_dynamic_field_settings.admin_allow_retrieve,
        )
        self.api_admin_dynamic_field_allow_create: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_CREATE",
            api_dynamic_field_settings.admin_allow_create,
        )
        self.api_admin_dynamic_field_allow_update: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_UPDATE",
            api_dynamic_field_settings.admin_allow_update,
        )
        self.api_admin_dynamic_field_allow_delete: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_DELETE",
            api_dynamic_field_settings.admin_allow_delete,
        )

        # FieldType-specific API settings
        self.api_field_type_serializer_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_FIELD_TYPE_SERIALIZER_CLASS",
            serializer_settings.field_type_serializer_class,
        )
        self.api_field_type_ordering_fields: List[str] = self.get_setting(
            f"{self.prefix}API_FIELD_TYPE_ORDERING_FIELDS",
            api_field_type_settings.ordering_fields,
        )
        self.api_field_type_search_fields: List[str] = self.get_setting(
            f"{self.prefix}API_FIELD_TYPE_SEARCH_FIELDS",
            api_field_type_settings.search_fields,
        )
        self.api_field_type_throttle_classes: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_FIELD_TYPE_THROTTLE_CLASSES",
            throttle_settings.throttle_class,
        )
        self.api_field_type_pagination_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_FIELD_TYPE_PAGINATION_CLASS",
            api_settings.pagination_class,
        )
        self.api_field_type_extra_permission_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_FIELD_TYPE_EXTRA_PERMISSION_CLASS",
                api_settings.extra_permission_class,
            )
        )
        self.api_field_type_parser_classes: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_FIELD_TYPE_PARSER_CLASSES",
            api_settings.parser_classes,
        )
        self.api_field_type_filterset_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_FIELD_TYPE_FILTERSET_CLASS",
            api_field_type_settings.filterset_class,
        )
        self.api_field_type_allow_list: bool = self.get_setting(
            f"{self.prefix}API_FIELD_TYPE_ALLOW_LIST",
            api_field_type_settings.allow_list,
        )
        self.api_field_type_allow_retrieve: bool = self.get_setting(
            f"{self.prefix}API_FIELD_TYPE_ALLOW_RETRIEVE",
            api_field_type_settings.allow_retrieve,
        )

        # AdminFieldType-specific API settings
        self.api_admin_field_type_serializer_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FIELD_TYPE_SERIALIZER_CLASS",
                serializer_settings.field_type_serializer_class,
            )
        )
        self.api_admin_field_type_ordering_fields: List[str] = self.get_setting(
            f"{self.prefix}API_ADMIN_FIELD_TYPE_ORDERING_FIELDS",
            api_field_type_settings.ordering_fields,
        )
        self.api_admin_field_type_search_fields: List[str] = self.get_setting(
            f"{self.prefix}API_ADMIN_FIELD_TYPE_SEARCH_FIELDS",
            api_field_type_settings.search_fields,
        )
        self.api_admin_field_type_throttle_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FIELD_TYPE_THROTTLE_CLASSES",
                throttle_settings.throttle_class,
            )
        )
        self.api_admin_field_type_pagination_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FIELD_TYPE_PAGINATION_CLASS",
                api_settings.pagination_class,
            )
        )
        self.api_admin_field_type_extra_permission_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FIELD_TYPE_EXTRA_PERMISSION_CLASS",
                api_settings.extra_permission_class,
            )
        )
        self.api_admin_field_type_parser_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FIELD_TYPE_PARSER_CLASSES",
                api_settings.parser_classes,
            )
        )
        self.api_admin_field_type_filterset_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FIELD_TYPE_FILTERSET_CLASS",
                api_field_type_settings.filterset_class,
            )
        )
        self.api_admin_field_type_allow_list: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_FIELD_TYPE_ALLOW_LIST",
            api_field_type_settings.admin_allow_list,
        )
        self.api_admin_field_type_allow_retrieve: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_FIELD_TYPE_ALLOW_RETRIEVE",
            api_field_type_settings.admin_allow_retrieve,
        )
        self.api_admin_field_type_allow_create: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_FIELD_TYPE_ALLOW_CREATE",
            api_field_type_settings.admin_allow_create,
        )
        self.api_admin_field_type_allow_update: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_FIELD_TYPE_ALLOW_UPDATE",
            api_field_type_settings.admin_allow_update,
        )
        self.api_admin_field_type_allow_delete: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_FIELD_TYPE_ALLOW_DELETE",
            api_field_type_settings.admin_allow_delete,
        )

        # FormSubmission-specific API settings
        self.api_form_submission_serializer_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_FORM_SUBMISSION_SERIALIZER_CLASS",
                serializer_settings.form_submission_serializer_class,
            )
        )
        self.api_form_submission_ordering_fields: List[str] = self.get_setting(
            f"{self.prefix}API_FORM_SUBMISSION_ORDERING_FIELDS",
            api_form_submission_settings.ordering_fields,
        )
        self.api_form_submission_search_fields: List[str] = self.get_setting(
            f"{self.prefix}API_FORM_SUBMISSION_SEARCH_FIELDS",
            api_form_submission_settings.search_fields,
        )
        self.api_form_submission_throttle_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_FORM_SUBMISSION_THROTTLE_CLASSES",
                throttle_settings.throttle_class,
            )
        )
        self.api_form_submission_pagination_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_FORM_SUBMISSION_PAGINATION_CLASS",
                api_settings.pagination_class,
            )
        )
        self.api_form_submission_extra_permission_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS",
                api_settings.extra_permission_class,
            )
        )
        self.api_form_submission_parser_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_FORM_SUBMISSION_PARSER_CLASSES",
                api_settings.parser_classes,
            )
        )
        self.api_form_submission_filterset_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_FORM_SUBMISSION_FILTERSET_CLASS",
                api_form_submission_settings.filterset_class,
            )
        )
        self.api_form_submission_allow_list: bool = self.get_setting(
            f"{self.prefix}API_FORM_SUBMISSION_ALLOW_LIST",
            api_form_submission_settings.allow_list,
        )
        self.api_form_submission_allow_retrieve: bool = self.get_setting(
            f"{self.prefix}API_FORM_SUBMISSION_ALLOW_RETRIEVE",
            api_form_submission_settings.allow_retrieve,
        )
        self.api_form_submission_allow_create: bool = self.get_setting(
            f"{self.prefix}API_FORM_SUBMISSION_ALLOW_CREATE",
            api_form_submission_settings.allow_create,
        )
        self.api_form_submission_allow_update: bool = self.get_setting(
            f"{self.prefix}API_FORM_SUBMISSION_ALLOW_UPDATE",
            api_form_submission_settings.allow_update,
        )
        self.api_form_submission_allow_delete: bool = self.get_setting(
            f"{self.prefix}API_FORM_SUBMISSION_ALLOW_DELETE",
            api_form_submission_settings.allow_delete,
        )

        # AdminFormSubmission-specific API settings
        self.api_admin_form_submission_serializer_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FORM_SUBMISSION_SERIALIZER_CLASS",
                serializer_settings.form_submission_serializer_class,
            )
        )
        self.api_admin_form_submission_ordering_fields: List[str] = self.get_setting(
            f"{self.prefix}API_ADMIN_FORM_SUBMISSION_ORDERING_FIELDS",
            api_form_submission_settings.ordering_fields,
        )
        self.api_admin_form_submission_search_fields: List[str] = self.get_setting(
            f"{self.prefix}API_ADMIN_FORM_SUBMISSION_SEARCH_FIELDS",
            api_form_submission_settings.search_fields,
        )
        self.api_admin_form_submission_throttle_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FORM_SUBMISSION_THROTTLE_CLASSES",
                throttle_settings.throttle_class,
            )
        )
        self.api_admin_form_submission_pagination_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FORM_SUBMISSION_PAGINATION_CLASS",
                api_settings.pagination_class,
            )
        )
        self.api_admin_form_submission_extra_permission_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS",
                api_settings.extra_permission_class,
            )
        )
        self.api_admin_form_submission_parser_classes: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FORM_SUBMISSION_PARSER_CLASSES",
                api_settings.parser_classes,
            )
        )
        self.api_admin_form_submission_filterset_class: OptionalPaths = (
            self.get_optional_paths(
                f"{self.prefix}API_ADMIN_FORM_SUBMISSION_FILTERSET_CLASS",
                api_form_submission_settings.filterset_class,
            )
        )
        self.api_admin_form_submission_allow_list: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_LIST",
            api_form_submission_settings.admin_allow_list,
        )
        self.api_admin_form_submission_allow_retrieve: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_RETRIEVE",
            api_form_submission_settings.admin_allow_retrieve,
        )
        self.api_admin_form_submission_allow_create: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_CREATE",
            api_form_submission_settings.admin_allow_create,
        )
        self.api_admin_form_submission_allow_update: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_UPDATE",
            api_form_submission_settings.admin_allow_update,
        )
        self.api_admin_form_submission_allow_delete: bool = self.get_setting(
            f"{self.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_DELETE",
            api_form_submission_settings.admin_allow_delete,
        )

    def get_setting(self, setting_name: str, default_value: Any) -> Any:
        """Retrieve a setting from Django settings with a default fallback.

        Args:
            setting_name (str): The name of the setting to retrieve.
            default_value (Any): The default value to return if the setting is not found.

        Returns:
            Any: The value of the setting or the default value if not found.

        """
        return getattr(settings, setting_name, default_value)

    def get_optional_paths(
        self,
        setting_name: str,
        default_path: DefaultPath,
    ) -> OptionalPaths:
        """Dynamically load a method or class path on a setting, or return None
        if the setting is None or invalid.

        Args:
            setting_name (str): The name of the setting for the method or class path.
            default_path (Optional[Union[str, List[str]]): The default import path for the method or class.

        Returns:
            Optional[Union[Type[Any], List[Type[Any]]]]: The imported method or class or None
             if import fails or the path is invalid.

        """
        _path: DefaultPath = self.get_setting(setting_name, default_path)

        if _path and isinstance(_path, str):
            try:
                return import_string(_path)
            except ImportError:
                return None
        elif _path and isinstance(_path, list):
            try:
                return [import_string(path) for path in _path if isinstance(path, str)]
            except ImportError:
                return []

        return None


# Create a global config object
config: DynamicFormConfig = DynamicFormConfig()
