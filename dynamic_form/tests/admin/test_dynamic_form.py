import sys

import pytest
from django.contrib import admin
from django.http import HttpRequest

from dynamic_form.admin import DynamicFormAdmin
from dynamic_form.models import DynamicForm
from dynamic_form.settings.conf import config
from dynamic_form.tests.constants import (
    PYTHON_VERSION,
    PYTHON_VERSION_REASON,
)

pytestmark = [
    pytest.mark.admin,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


@pytest.mark.django_db
class TestDynamicFormAdmin:
    """
    Tests for the DynamicFormAdmin class in the Django admin interface.

    This test class verifies the general functionality of the DynamicFormAdmin,
    ensuring it is properly configured and behaves as expected in the Django admin
    interface, with a focus on configuration and permissions.

    Tests:
    -------
    - test_admin_registered: Verifies DynamicForm is registered with DynamicFormAdmin.
    - test_list_display_configured: Ensures list_display is properly set.
    - test_list_filter_configured: Ensures list_filter is properly set.
    - test_search_fields_configured: Ensures search_fields is properly set.
    - test_admin_permissions: Verifies permission settings via config.
    - test_readonly_fields: Ensures readonly_fields are correctly configured.
    - test_list_display_links: Verifies list_display_links configuration.
    - test_dynamic_form_display: Tests display of DynamicForm fields in list view.
    """

    def test_admin_registered(self):
        """
        Test that the DynamicForm model is registered with DynamicFormAdmin in the admin site.

        Asserts:
        --------
            The admin site has DynamicForm registered with an instance of DynamicFormAdmin.
        """
        assert isinstance(admin.site._registry[DynamicForm], DynamicFormAdmin)

    def test_list_display_configured(
        self, dynamic_form_admin: DynamicFormAdmin
    ) -> None:
        """
        Test that the list_display attribute is defined and non-empty.

        Args:
            dynamic_form_admin (DynamicFormAdmin): The admin class instance being tested.

        Asserts:
        --------
            list_display is a tuple or list and has at least one item.
        """
        assert isinstance(dynamic_form_admin.list_display, (tuple, list))
        assert len(dynamic_form_admin.list_display) > 0

    def test_list_filter_configured(self, dynamic_form_admin: DynamicFormAdmin) -> None:
        """
        Test that the list_filter attribute is defined and non-empty.

        Args:
            dynamic_form_admin (DynamicFormAdmin): The admin class instance being tested.

        Asserts:
        --------
            list_filter is a tuple or list and has at least one item.
        """
        assert isinstance(dynamic_form_admin.list_filter, (tuple, list))
        assert len(dynamic_form_admin.list_filter) > 0

    def test_search_fields_configured(
        self, dynamic_form_admin: DynamicFormAdmin
    ) -> None:
        """
        Test that the search_fields attribute is defined and non-empty.

        Args:
            dynamic_form_admin (DynamicFormAdmin): The admin class instance being tested.

        Asserts:
        --------
            search_fields is a tuple or list and has at least one item.
        """
        assert isinstance(dynamic_form_admin.search_fields, (tuple, list))
        assert len(dynamic_form_admin.search_fields) > 0

    def test_admin_permissions(
        self, dynamic_form_admin: DynamicFormAdmin, mock_request: HttpRequest
    ):
        """
        Test that admin permissions reflect the config settings.

        Args:
            dynamic_form_admin (DynamicFormAdmin): The admin class instance being tested.
            mock_request (HttpRequest): A mock request object for permission checks.

        Asserts:
        --------
            has_add_permission, has_change_permission, has_delete_permission, and
            has_module_permission reflect config settings via AdminPermissionControlMixin.
        """
        # Test with config permissions denied
        config.admin_has_add_permission = False
        config.admin_has_change_permission = False
        config.admin_has_delete_permission = False
        config.admin_has_module_permission = False
        assert dynamic_form_admin.has_add_permission(mock_request) is False
        assert dynamic_form_admin.has_change_permission(mock_request) is False
        assert dynamic_form_admin.has_delete_permission(mock_request) is False
        assert dynamic_form_admin.has_module_permission(mock_request) is False

        # Test with config permissions granted
        config.admin_has_add_permission = True
        config.admin_has_change_permission = True
        config.admin_has_delete_permission = True
        config.admin_has_module_permission = True
        assert dynamic_form_admin.has_add_permission(mock_request) is True
        assert dynamic_form_admin.has_change_permission(mock_request) is True
        assert dynamic_form_admin.has_delete_permission(mock_request) is True
        assert dynamic_form_admin.has_module_permission(mock_request) is True

    def test_readonly_fields(self, dynamic_form_admin: DynamicFormAdmin) -> None:
        """
        Test that readonly_fields are properly configured.

        Args:
            dynamic_form_admin (DynamicFormAdmin): The admin class instance being tested.

        Asserts:
        --------
            readonly_fields includes expected fields.
        """
        expected_fields = {"created_at", "updated_at"}
        assert isinstance(dynamic_form_admin.readonly_fields, (tuple, list))
        assert set(dynamic_form_admin.readonly_fields) == expected_fields

    def test_list_display_links(self, dynamic_form_admin: DynamicFormAdmin) -> None:
        """
        Test that list_display_links is properly configured.

        Args:
            dynamic_form_admin (DynamicFormAdmin): The admin class instance being tested.

        Asserts:
        --------
            list_display_links matches the expected fields.
        """
        expected_links = {"id", "name"}
        assert isinstance(dynamic_form_admin.list_display_links, (tuple, list))
        assert set(dynamic_form_admin.list_display_links) == expected_links
