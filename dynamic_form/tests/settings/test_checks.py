import sys
from unittest.mock import MagicMock, patch

import pytest

from dynamic_form.settings.checks import check_dynamic_form_settings
from dynamic_form.tests.constants import (
    PYTHON_VERSION,
    PYTHON_VERSION_REASON,
)

pytestmark = [
    pytest.mark.settings,
    pytest.mark.settings_checks,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


class TestDynamicFormSettings:
    @patch("dynamic_form.settings.checks.config")
    def test_valid_settings(self, mock_config: MagicMock) -> None:
        """
        Test that valid settings produce no errors.

        Args:
            mock_config (MagicMock): Mocked configuration object with valid settings.

        Asserts:
            No errors are returned when all settings are valid.
        """
        # Mock all config values to be valid
        # Admin settings
        mock_config.admin_has_add_permission = True
        mock_config.admin_has_change_permission = False
        mock_config.admin_has_delete_permission = True
        mock_config.admin_has_module_permission = False

        # Global API settings
        mock_config.base_user_throttle_rate = "100/day"
        mock_config.staff_user_throttle_rate = "200/hour"
        mock_config.user_serializer_fields = ["id", "username"]

        # DynamicForm API settings
        mock_config.api_dynamic_form_allow_list = True
        mock_config.api_dynamic_form_allow_retrieve = False
        mock_config.api_dynamic_form_ordering_fields = ["name", "created_at"]
        mock_config.api_dynamic_form_search_fields = ["name"]
        mock_config.api_dynamic_form_extra_permission_class = None
        mock_config.api_dynamic_form_filterset_class = None

        # AdminDynamicForm API settings
        mock_config.api_admin_dynamic_form_allow_list = True
        mock_config.api_admin_dynamic_form_allow_retrieve = False
        mock_config.api_admin_dynamic_form_allow_create = True
        mock_config.api_admin_dynamic_form_allow_update = False
        mock_config.api_admin_dynamic_form_allow_delete = True
        mock_config.api_admin_dynamic_form_serializer_class = None
        mock_config.api_admin_dynamic_form_ordering_fields = ["name"]
        mock_config.api_admin_dynamic_form_search_fields = ["name"]
        mock_config.api_admin_dynamic_form_throttle_classes = None
        mock_config.api_admin_dynamic_form_pagination_class = None
        mock_config.api_admin_dynamic_form_extra_permission_class = None
        mock_config.api_admin_dynamic_form_parser_classes = None
        mock_config.api_admin_dynamic_form_filterset_class = None

        # DynamicField API settings
        mock_config.api_dynamic_field_allow_list = True
        mock_config.api_dynamic_field_allow_retrieve = False
        mock_config.api_dynamic_field_serializer_class = None
        mock_config.api_dynamic_field_ordering_fields = ["name"]
        mock_config.api_dynamic_field_search_fields = ["name"]
        mock_config.api_dynamic_field_throttle_classes = None
        mock_config.api_dynamic_field_pagination_class = None
        mock_config.api_dynamic_field_extra_permission_class = None
        mock_config.api_dynamic_field_parser_classes = None
        mock_config.api_dynamic_field_filterset_class = None

        # AdminDynamicField API settings
        mock_config.api_admin_dynamic_field_allow_list = True
        mock_config.api_admin_dynamic_field_allow_retrieve = False
        mock_config.api_admin_dynamic_field_allow_create = True
        mock_config.api_admin_dynamic_field_allow_update = False
        mock_config.api_admin_dynamic_field_allow_delete = True
        mock_config.api_admin_dynamic_field_serializer_class = None
        mock_config.api_admin_dynamic_field_ordering_fields = ["name"]
        mock_config.api_admin_dynamic_field_search_fields = ["name"]
        mock_config.api_admin_dynamic_field_throttle_classes = None
        mock_config.api_admin_dynamic_field_pagination_class = None
        mock_config.api_admin_dynamic_field_extra_permission_class = None
        mock_config.api_admin_dynamic_field_parser_classes = None
        mock_config.api_admin_dynamic_field_filterset_class = None

        # FieldType API settings
        mock_config.api_field_type_allow_list = True
        mock_config.api_field_type_allow_retrieve = False
        mock_config.api_field_type_serializer_class = None
        mock_config.api_field_type_ordering_fields = ["name"]
        mock_config.api_field_type_search_fields = ["name"]
        mock_config.api_field_type_throttle_classes = None
        mock_config.api_field_type_pagination_class = None
        mock_config.api_field_type_extra_permission_class = None
        mock_config.api_field_type_parser_classes = None
        mock_config.api_field_type_filterset_class = None

        # AdminFieldType API settings
        mock_config.api_admin_field_type_allow_list = True
        mock_config.api_admin_field_type_allow_retrieve = False
        mock_config.api_admin_field_type_allow_create = True
        mock_config.api_admin_field_type_allow_update = False
        mock_config.api_admin_field_type_allow_delete = True
        mock_config.api_admin_field_type_serializer_class = None
        mock_config.api_admin_field_type_ordering_fields = ["name"]
        mock_config.api_admin_field_type_search_fields = ["name"]
        mock_config.api_admin_field_type_throttle_classes = None
        mock_config.api_admin_field_type_pagination_class = None
        mock_config.api_admin_field_type_extra_permission_class = None
        mock_config.api_admin_field_type_parser_classes = None
        mock_config.api_admin_field_type_filterset_class = None

        # FormSubmission API settings
        mock_config.api_form_submission_allow_list = True
        mock_config.api_form_submission_allow_retrieve = False
        mock_config.api_form_submission_allow_create = True
        mock_config.api_form_submission_allow_update = False
        mock_config.api_form_submission_allow_delete = True
        mock_config.api_form_submission_serializer_class = None
        mock_config.api_form_submission_ordering_fields = ["submitted_at"]
        mock_config.api_form_submission_search_fields = ["form__name"]
        mock_config.api_form_submission_throttle_classes = None
        mock_config.api_form_submission_pagination_class = None
        mock_config.api_form_submission_extra_permission_class = None
        mock_config.api_form_submission_parser_classes = None
        mock_config.api_form_submission_filterset_class = None

        # AdminFormSubmission API settings
        mock_config.api_admin_form_submission_allow_list = True
        mock_config.api_admin_form_submission_allow_retrieve = False
        mock_config.api_admin_form_submission_allow_create = True
        mock_config.api_admin_form_submission_allow_update = False
        mock_config.api_admin_form_submission_allow_delete = True
        mock_config.api_admin_form_submission_serializer_class = None
        mock_config.api_admin_form_submission_ordering_fields = ["submitted_at"]
        mock_config.api_admin_form_submission_search_fields = ["form__name"]
        mock_config.api_admin_form_submission_throttle_classes = None
        mock_config.api_admin_form_submission_pagination_class = None
        mock_config.api_admin_form_submission_extra_permission_class = None
        mock_config.api_admin_form_submission_parser_classes = None
        mock_config.api_admin_form_submission_filterset_class = None

        mock_config.get_setting.side_effect = lambda name, default: default

        errors = check_dynamic_form_settings(None)
        assert not errors, f"Expected no errors for valid settings, but got {errors}"

    @patch("dynamic_form.settings.checks.config")
    def test_invalid_boolean_settings(self, mock_config: MagicMock) -> None:
        """
        Test that invalid boolean settings return errors.

        Args:
            mock_config (MagicMock): Mocked configuration object with invalid boolean settings.

        Asserts:
            Errors are returned for invalid boolean values in settings.
        """
        # Set valid defaults for non-boolean settings
        # Global API settings
        mock_config.base_user_throttle_rate = "100/day"
        mock_config.staff_user_throttle_rate = "200/hour"
        mock_config.user_serializer_fields = ["id", "username"]

        # DynamicForm API settings
        mock_config.api_dynamic_form_ordering_fields = ["name", "created_at"]
        mock_config.api_dynamic_form_search_fields = ["name"]

        # AdminDynamicForm API settings
        mock_config.api_admin_dynamic_form_ordering_fields = ["name"]
        mock_config.api_admin_dynamic_form_search_fields = ["name"]

        # DynamicField API settings
        mock_config.api_dynamic_field_ordering_fields = ["name"]
        mock_config.api_dynamic_field_search_fields = ["name"]

        # AdminDynamicField API settings
        mock_config.api_admin_dynamic_field_ordering_fields = ["name"]
        mock_config.api_admin_dynamic_field_search_fields = ["name"]

        # FieldType API settings
        mock_config.api_field_type_ordering_fields = ["name"]
        mock_config.api_field_type_search_fields = ["name"]

        # AdminFieldType API settings
        mock_config.api_admin_field_type_ordering_fields = ["name"]
        mock_config.api_admin_field_type_search_fields = ["name"]

        # FormSubmission API settings
        mock_config.api_form_submission_ordering_fields = ["submitted_at"]
        mock_config.api_form_submission_search_fields = ["form__name"]

        # AdminFormSubmission API settings
        mock_config.api_admin_form_submission_ordering_fields = ["submitted_at"]
        mock_config.api_admin_form_submission_search_fields = ["form__name"]

        # Invalid boolean settings
        mock_config.admin_has_add_permission = "not_boolean"
        mock_config.admin_has_change_permission = "not_boolean"
        mock_config.admin_has_delete_permission = "not_boolean"
        mock_config.admin_has_module_permission = "not_boolean"
        mock_config.api_dynamic_form_allow_list = "not_boolean"
        mock_config.api_dynamic_form_allow_retrieve = "not_boolean"
        mock_config.api_admin_dynamic_form_allow_list = "not_boolean"
        mock_config.api_admin_dynamic_form_allow_retrieve = "not_boolean"
        mock_config.api_admin_dynamic_form_allow_create = "not_boolean"
        mock_config.api_admin_dynamic_form_allow_update = "not_boolean"
        mock_config.api_admin_dynamic_form_allow_delete = "not_boolean"
        mock_config.api_dynamic_field_allow_list = "not_boolean"
        mock_config.api_dynamic_field_allow_retrieve = "not_boolean"
        mock_config.api_admin_dynamic_field_allow_list = "not_boolean"
        mock_config.api_admin_dynamic_field_allow_retrieve = "not_boolean"
        mock_config.api_admin_dynamic_field_allow_create = "not_boolean"
        mock_config.api_admin_dynamic_field_allow_update = "not_boolean"
        mock_config.api_admin_dynamic_field_allow_delete = "not_boolean"
        mock_config.api_field_type_allow_list = "not_boolean"
        mock_config.api_field_type_allow_retrieve = "not_boolean"
        mock_config.api_admin_field_type_allow_list = "not_boolean"
        mock_config.api_admin_field_type_allow_retrieve = "not_boolean"
        mock_config.api_admin_field_type_allow_create = "not_boolean"
        mock_config.api_admin_field_type_allow_update = "not_boolean"
        mock_config.api_admin_field_type_allow_delete = "not_boolean"
        mock_config.api_form_submission_allow_list = "not_boolean"
        mock_config.api_form_submission_allow_retrieve = "not_boolean"
        mock_config.api_form_submission_allow_create = "not_boolean"
        mock_config.api_form_submission_allow_update = "not_boolean"
        mock_config.api_form_submission_allow_delete = "not_boolean"
        mock_config.api_admin_form_submission_allow_list = "not_boolean"
        mock_config.api_admin_form_submission_allow_retrieve = "not_boolean"
        mock_config.api_admin_form_submission_allow_create = "not_boolean"
        mock_config.api_admin_form_submission_allow_update = "not_boolean"
        mock_config.api_admin_form_submission_allow_delete = "not_boolean"

        mock_config.get_setting.side_effect = lambda name, default: default

        errors = check_dynamic_form_settings(None)
        assert (
            len(errors) == 35
        ), f"Expected 35 errors for invalid booleans, but got {len(errors)}"
        error_ids = [error.id for error in errors]
        expected_ids = [
            f"dynamic_form.E001_{mock_config.prefix}ADMIN_HAS_ADD_PERMISSION",
            f"dynamic_form.E001_{mock_config.prefix}ADMIN_HAS_CHANGE_PERMISSION",
            f"dynamic_form.E001_{mock_config.prefix}ADMIN_HAS_DELETE_PERMISSION",
            f"dynamic_form.E001_{mock_config.prefix}ADMIN_HAS_MODULE_PERMISSION",
            f"dynamic_form.E001_{mock_config.prefix}API_DYNAMIC_FORM_ALLOW_LIST",
            f"dynamic_form.E001_{mock_config.prefix}API_DYNAMIC_FORM_ALLOW_RETRIEVE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_LIST",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_RETRIEVE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_CREATE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_UPDATE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_ALLOW_DELETE",
            f"dynamic_form.E001_{mock_config.prefix}API_DYNAMIC_FIELD_ALLOW_LIST",
            f"dynamic_form.E001_{mock_config.prefix}API_DYNAMIC_FIELD_ALLOW_RETRIEVE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_LIST",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_RETRIEVE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_CREATE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_UPDATE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_ALLOW_DELETE",
            f"dynamic_form.E001_{mock_config.prefix}API_FIELD_TYPE_ALLOW_LIST",
            f"dynamic_form.E001_{mock_config.prefix}API_FIELD_TYPE_ALLOW_RETRIEVE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_FIELD_TYPE_ALLOW_LIST",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_FIELD_TYPE_ALLOW_RETRIEVE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_FIELD_TYPE_ALLOW_CREATE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_FIELD_TYPE_ALLOW_UPDATE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_FIELD_TYPE_ALLOW_DELETE",
            f"dynamic_form.E001_{mock_config.prefix}API_FORM_SUBMISSION_ALLOW_LIST",
            f"dynamic_form.E001_{mock_config.prefix}API_FORM_SUBMISSION_ALLOW_RETRIEVE",
            f"dynamic_form.E001_{mock_config.prefix}API_FORM_SUBMISSION_ALLOW_CREATE",
            f"dynamic_form.E001_{mock_config.prefix}API_FORM_SUBMISSION_ALLOW_UPDATE",
            f"dynamic_form.E001_{mock_config.prefix}API_FORM_SUBMISSION_ALLOW_DELETE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_LIST",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_RETRIEVE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_CREATE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_UPDATE",
            f"dynamic_form.E001_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_ALLOW_DELETE",
        ]
        assert all(
            eid in error_ids for eid in expected_ids
        ), f"Expected error IDs {expected_ids}, got {error_ids}"

    @patch("dynamic_form.settings.checks.config")
    def test_invalid_list_settings(self, mock_config: MagicMock) -> None:
        """
        Test that invalid list settings return errors.

        Args:
            mock_config (MagicMock): Mocked configuration object with invalid list settings.

        Asserts:
            Errors are returned for invalid list values in settings.
        """
        # Valid boolean and throttle settings
        mock_config.admin_has_add_permission = True
        mock_config.admin_has_change_permission = False
        mock_config.admin_has_delete_permission = True
        mock_config.admin_has_module_permission = False
        mock_config.base_user_throttle_rate = "100/day"
        mock_config.staff_user_throttle_rate = "200/hour"
        mock_config.api_dynamic_form_allow_list = True
        mock_config.api_dynamic_form_allow_retrieve = False
        mock_config.api_admin_dynamic_form_allow_list = True
        mock_config.api_admin_dynamic_form_allow_retrieve = False
        mock_config.api_admin_dynamic_form_allow_create = True
        mock_config.api_admin_dynamic_form_allow_update = False
        mock_config.api_admin_dynamic_form_allow_delete = True
        mock_config.api_dynamic_field_allow_list = True
        mock_config.api_dynamic_field_allow_retrieve = False
        mock_config.api_admin_dynamic_field_allow_list = True
        mock_config.api_admin_dynamic_field_allow_retrieve = False
        mock_config.api_admin_dynamic_field_allow_create = True
        mock_config.api_admin_dynamic_field_allow_update = False
        mock_config.api_admin_dynamic_field_allow_delete = True
        mock_config.api_field_type_allow_list = True
        mock_config.api_field_type_allow_retrieve = False
        mock_config.api_admin_field_type_allow_list = True
        mock_config.api_admin_field_type_allow_retrieve = False
        mock_config.api_admin_field_type_allow_create = True
        mock_config.api_admin_field_type_allow_update = False
        mock_config.api_admin_field_type_allow_delete = True
        mock_config.api_form_submission_allow_list = True
        mock_config.api_form_submission_allow_retrieve = False
        mock_config.api_form_submission_allow_create = True
        mock_config.api_form_submission_allow_update = False
        mock_config.api_form_submission_allow_delete = True
        mock_config.api_admin_form_submission_allow_list = True
        mock_config.api_admin_form_submission_allow_retrieve = False
        mock_config.api_admin_form_submission_allow_create = True
        mock_config.api_admin_form_submission_allow_update = False
        mock_config.api_admin_form_submission_allow_delete = True

        # Invalid list settings
        mock_config.user_serializer_fields = [123]  # Invalid type
        mock_config.api_dynamic_form_ordering_fields = []  # Empty list
        mock_config.api_dynamic_form_search_fields = [456]  # Invalid type
        mock_config.api_admin_dynamic_form_ordering_fields = []  # Empty list
        mock_config.api_admin_dynamic_form_search_fields = [789]  # Invalid type
        mock_config.api_dynamic_field_ordering_fields = []  # Empty list
        mock_config.api_dynamic_field_search_fields = [101]  # Invalid type
        mock_config.api_admin_dynamic_field_ordering_fields = []  # Empty list
        mock_config.api_admin_dynamic_field_search_fields = [112]  # Invalid type
        mock_config.api_field_type_ordering_fields = []  # Empty list
        mock_config.api_field_type_search_fields = [131]  # Invalid type
        mock_config.api_admin_field_type_ordering_fields = []  # Empty list
        mock_config.api_admin_field_type_search_fields = [141]  # Invalid type
        mock_config.api_form_submission_ordering_fields = []  # Empty list
        mock_config.api_form_submission_search_fields = [151]  # Invalid type
        mock_config.api_admin_form_submission_ordering_fields = []  # Empty list
        mock_config.api_admin_form_submission_search_fields = [161]  # Invalid type

        mock_config.get_setting.side_effect = lambda name, default: default

        errors = check_dynamic_form_settings(None)
        assert (
            len(errors) == 17
        ), f"Expected 17 errors for invalid lists, but got {len(errors)}"
        error_ids = [error.id for error in errors]
        expected_ids = [
            f"dynamic_form.E004_{mock_config.prefix}API_USER_SERIALIZER_FIELDS",
            f"dynamic_form.E003_{mock_config.prefix}API_DYNAMIC_FORM_ORDERING_FIELDS",
            f"dynamic_form.E004_{mock_config.prefix}API_DYNAMIC_FORM_SEARCH_FIELDS",
            f"dynamic_form.E003_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_ORDERING_FIELDS",
            f"dynamic_form.E004_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_SEARCH_FIELDS",
            f"dynamic_form.E003_{mock_config.prefix}API_DYNAMIC_FIELD_ORDERING_FIELDS",
            f"dynamic_form.E004_{mock_config.prefix}API_DYNAMIC_FIELD_SEARCH_FIELDS",
            f"dynamic_form.E003_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_ORDERING_FIELDS",
            f"dynamic_form.E004_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_SEARCH_FIELDS",
            f"dynamic_form.E003_{mock_config.prefix}API_FIELD_TYPE_ORDERING_FIELDS",
            f"dynamic_form.E004_{mock_config.prefix}API_FIELD_TYPE_SEARCH_FIELDS",
            f"dynamic_form.E003_{mock_config.prefix}API_ADMIN_FIELD_TYPE_ORDERING_FIELDS",
            f"dynamic_form.E004_{mock_config.prefix}API_ADMIN_FIELD_TYPE_SEARCH_FIELDS",
            f"dynamic_form.E003_{mock_config.prefix}API_FORM_SUBMISSION_ORDERING_FIELDS",
            f"dynamic_form.E004_{mock_config.prefix}API_FORM_SUBMISSION_SEARCH_FIELDS",
            f"dynamic_form.E003_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_ORDERING_FIELDS",
            f"dynamic_form.E004_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_SEARCH_FIELDS",
        ]
        assert all(
            eid in error_ids for eid in expected_ids
        ), f"Expected error IDs {expected_ids}, got {error_ids}"

    @patch("dynamic_form.settings.checks.config")
    def test_invalid_throttle_rate(self, mock_config: MagicMock) -> None:
        """
        Test that invalid throttle rates return errors.

        Args:
            mock_config (MagicMock): Mocked configuration object with invalid throttle rates.

        Asserts:
            Errors are returned for invalid throttle rates.
        """
        # Valid boolean and list settings
        mock_config.admin_has_add_permission = True
        mock_config.admin_has_change_permission = False
        mock_config.admin_has_delete_permission = True
        mock_config.admin_has_module_permission = False
        mock_config.api_dynamic_form_allow_list = True
        mock_config.api_dynamic_form_allow_retrieve = False
        mock_config.api_admin_dynamic_form_allow_list = True
        mock_config.api_admin_dynamic_form_allow_retrieve = False
        mock_config.api_admin_dynamic_form_allow_create = True
        mock_config.api_admin_dynamic_form_allow_update = False
        mock_config.api_admin_dynamic_form_allow_delete = True
        mock_config.api_dynamic_field_allow_list = True
        mock_config.api_dynamic_field_allow_retrieve = False
        mock_config.api_admin_dynamic_field_allow_list = True
        mock_config.api_admin_dynamic_field_allow_retrieve = False
        mock_config.api_admin_dynamic_field_allow_create = True
        mock_config.api_admin_dynamic_field_allow_update = False
        mock_config.api_admin_dynamic_field_allow_delete = True
        mock_config.api_field_type_allow_list = True
        mock_config.api_field_type_allow_retrieve = False
        mock_config.api_admin_field_type_allow_list = True
        mock_config.api_admin_field_type_allow_retrieve = False
        mock_config.api_admin_field_type_allow_create = True
        mock_config.api_admin_field_type_allow_update = False
        mock_config.api_admin_field_type_allow_delete = True
        mock_config.api_form_submission_allow_list = True
        mock_config.api_form_submission_allow_retrieve = False
        mock_config.api_form_submission_allow_create = True
        mock_config.api_form_submission_allow_update = False
        mock_config.api_form_submission_allow_delete = True
        mock_config.api_admin_form_submission_allow_list = True
        mock_config.api_admin_form_submission_allow_retrieve = False
        mock_config.api_admin_form_submission_allow_create = True
        mock_config.api_admin_form_submission_allow_update = False
        mock_config.api_admin_form_submission_allow_delete = True
        mock_config.user_serializer_fields = ["id", "username"]
        mock_config.api_dynamic_form_ordering_fields = ["name"]
        mock_config.api_dynamic_form_search_fields = ["name"]
        mock_config.api_admin_dynamic_form_ordering_fields = ["name"]
        mock_config.api_admin_dynamic_form_search_fields = ["name"]
        mock_config.api_dynamic_field_ordering_fields = ["name"]
        mock_config.api_dynamic_field_search_fields = ["name"]
        mock_config.api_admin_dynamic_field_ordering_fields = ["name"]
        mock_config.api_admin_dynamic_field_search_fields = ["name"]
        mock_config.api_field_type_ordering_fields = ["name"]
        mock_config.api_field_type_search_fields = ["name"]
        mock_config.api_admin_field_type_ordering_fields = ["name"]
        mock_config.api_admin_field_type_search_fields = ["name"]
        mock_config.api_form_submission_ordering_fields = ["submitted_at"]
        mock_config.api_form_submission_search_fields = ["form__name"]
        mock_config.api_admin_form_submission_ordering_fields = ["submitted_at"]
        mock_config.api_admin_form_submission_search_fields = ["form__name"]

        # Invalid throttle rates
        mock_config.base_user_throttle_rate = "invalid_rate"
        mock_config.staff_user_throttle_rate = "abc/hour"

        mock_config.get_setting.side_effect = lambda name, default: default

        errors = check_dynamic_form_settings(None)
        assert (
            len(errors) == 2
        ), f"Expected 2 errors for invalid throttle rates, but got {len(errors)}"
        error_ids = [error.id for error in errors]
        expected_ids = [
            f"dynamic_form.E005_{mock_config.prefix}BASE_USER_THROTTLE_RATE",
            f"dynamic_form.E007_{mock_config.prefix}STAFF_USER_THROTTLE_RATE",
        ]
        assert all(
            eid in error_ids for eid in expected_ids
        ), f"Expected error IDs {expected_ids}, got {error_ids}"

    @patch("dynamic_form.settings.checks.config")
    def test_invalid_path_import(self, mock_config: MagicMock) -> None:
        """
        Test that invalid path import settings return errors.

        Args:
            mock_config (MagicMock): Mocked configuration object with invalid paths.

        Asserts:
            Errors are returned for invalid path imports.
        """
        # Valid boolean, list, and throttle settings
        mock_config.admin_has_add_permission = True
        mock_config.admin_has_change_permission = False
        mock_config.admin_has_delete_permission = True
        mock_config.admin_has_module_permission = False
        mock_config.api_dynamic_form_allow_list = True
        mock_config.api_dynamic_form_allow_retrieve = False
        mock_config.api_admin_dynamic_form_allow_list = True
        mock_config.api_admin_dynamic_form_allow_retrieve = False
        mock_config.api_admin_dynamic_form_allow_create = True
        mock_config.api_admin_dynamic_form_allow_update = False
        mock_config.api_admin_dynamic_form_allow_delete = True
        mock_config.api_dynamic_field_allow_list = True
        mock_config.api_dynamic_field_allow_retrieve = False
        mock_config.api_admin_dynamic_field_allow_list = True
        mock_config.api_admin_dynamic_field_allow_retrieve = False
        mock_config.api_admin_dynamic_field_allow_create = True
        mock_config.api_admin_dynamic_field_allow_update = False
        mock_config.api_admin_dynamic_field_allow_delete = True
        mock_config.api_field_type_allow_list = True
        mock_config.api_field_type_allow_retrieve = False
        mock_config.api_admin_field_type_allow_list = True
        mock_config.api_admin_field_type_allow_retrieve = False
        mock_config.api_admin_field_type_allow_create = True
        mock_config.api_admin_field_type_allow_update = False
        mock_config.api_admin_field_type_allow_delete = True
        mock_config.api_form_submission_allow_list = True
        mock_config.api_form_submission_allow_retrieve = False
        mock_config.api_form_submission_allow_create = True
        mock_config.api_form_submission_allow_update = False
        mock_config.api_form_submission_allow_delete = True
        mock_config.api_admin_form_submission_allow_list = True
        mock_config.api_admin_form_submission_allow_retrieve = False
        mock_config.api_admin_form_submission_allow_create = True
        mock_config.api_admin_form_submission_allow_update = False
        mock_config.api_admin_form_submission_allow_delete = True
        mock_config.base_user_throttle_rate = "100/day"
        mock_config.staff_user_throttle_rate = "200/hour"
        mock_config.user_serializer_fields = ["id", "username"]
        mock_config.api_dynamic_form_ordering_fields = ["name"]
        mock_config.api_dynamic_form_search_fields = ["name"]
        mock_config.api_admin_dynamic_form_ordering_fields = ["name"]
        mock_config.api_admin_dynamic_form_search_fields = ["name"]
        mock_config.api_dynamic_field_ordering_fields = ["name"]
        mock_config.api_dynamic_field_search_fields = ["name"]
        mock_config.api_admin_dynamic_field_ordering_fields = ["name"]
        mock_config.api_admin_dynamic_field_search_fields = ["name"]
        mock_config.api_field_type_ordering_fields = ["name"]
        mock_config.api_field_type_search_fields = ["name"]
        mock_config.api_admin_field_type_ordering_fields = ["name"]
        mock_config.api_admin_field_type_search_fields = ["name"]
        mock_config.api_form_submission_ordering_fields = ["submitted_at"]
        mock_config.api_form_submission_search_fields = ["form__name"]
        mock_config.api_admin_form_submission_ordering_fields = ["submitted_at"]
        mock_config.api_admin_form_submission_search_fields = ["form__name"]

        # Invalid path imports
        mock_config.get_setting.side_effect = (
            lambda name, default: "invalid.path.ClassName"
        )

        errors = check_dynamic_form_settings(None)
        assert (
            len(errors) == 51
        ), f"Expected 51 errors for invalid paths, but got {len(errors)}"
        error_ids = [error.id for error in errors]
        expected_ids = [
            f"dynamic_form.E010_{mock_config.prefix}ADMIN_SITE_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_PERMISSION_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_USER_SERIALIZER_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_DYNAMIC_FORM_SERIALIZER_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_DYNAMIC_FORM_THROTTLE_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_DYNAMIC_FORM_PAGINATION_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_DYNAMIC_FORM_PARSER_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_DYNAMIC_FORM_FILTERSET_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_SERIALIZER_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_THROTTLE_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_PAGINATION_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_PARSER_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_DYNAMIC_FORM_FILTERSET_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_DYNAMIC_FIELD_SERIALIZER_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_DYNAMIC_FIELD_THROTTLE_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_DYNAMIC_FIELD_PAGINATION_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_DYNAMIC_FIELD_PARSER_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_DYNAMIC_FIELD_FILTERSET_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_SERIALIZER_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_THROTTLE_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_PAGINATION_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_PARSER_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_DYNAMIC_FIELD_FILTERSET_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_FIELD_TYPE_SERIALIZER_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_FIELD_TYPE_THROTTLE_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_FIELD_TYPE_PAGINATION_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_FIELD_TYPE_EXTRA_PERMISSION_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_FIELD_TYPE_PARSER_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_FIELD_TYPE_FILTERSET_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_FIELD_TYPE_SERIALIZER_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_ADMIN_FIELD_TYPE_THROTTLE_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_FIELD_TYPE_PAGINATION_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_FIELD_TYPE_EXTRA_PERMISSION_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_ADMIN_FIELD_TYPE_PARSER_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_FIELD_TYPE_FILTERSET_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_FORM_SUBMISSION_SERIALIZER_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_FORM_SUBMISSION_THROTTLE_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_FORM_SUBMISSION_PAGINATION_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_FORM_SUBMISSION_PARSER_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_FORM_SUBMISSION_FILTERSET_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_SERIALIZER_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_THROTTLE_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_PAGINATION_CLASS",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS",
            f"dynamic_form.E011_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_PARSER_CLASSES",
            f"dynamic_form.E010_{mock_config.prefix}API_ADMIN_FORM_SUBMISSION_FILTERSET_CLASS",
        ]
        assert all(
            eid in error_ids for eid in expected_ids
        ), f"Expected error IDs {expected_ids}, got {error_ids}"
