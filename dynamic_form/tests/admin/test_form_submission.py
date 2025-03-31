import sys

import pytest
from django.contrib import admin
from django.http import HttpRequest

from dynamic_form.admin import FormSubmissionAdmin
from dynamic_form.models import FormSubmission
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
class TestFormSubmissionAdmin:
    """
    Tests for the FormSubmissionAdmin class in the Django admin interface.

    This test class verifies the general functionality of the FormSubmissionAdmin,
    ensuring it is properly configured and behaves as expected in the Django admin
    interface, with a focus on permissions and display settings.

    Tests:
    -------
    - test_admin_registered: Verifies FormSubmission is registered with FormSubmissionAdmin.
    - test_list_display_configured: Ensures list_display is properly set.
    - test_list_filter_configured: Ensures list_filter is properly set.
    - test_search_fields_configured: Ensures search_fields is properly set.
    - test_admin_permissions: Verifies permission settings, including overrides.
    """

    def test_admin_registered(self):
        """
        Test that the FormSubmission model is registered with FormSubmissionAdmin in the admin site.

        Asserts:
        --------
            The admin site has FormSubmission registered with an instance of FormSubmissionAdmin.
        """
        assert isinstance(admin.site._registry[FormSubmission], FormSubmissionAdmin)

    def test_list_display_configured(
        self, form_submission_admin: FormSubmissionAdmin
    ) -> None:
        """
        Test that the list_display attribute is defined and non-empty.

        Args:
            form_submission_admin (FormSubmissionAdmin): The admin class instance being tested.

        Asserts:
        --------
            list_display is a tuple or list and has at least one item.
        """
        assert isinstance(form_submission_admin.list_display, (tuple, list))
        assert len(form_submission_admin.list_display) > 0

    def test_list_filter_configured(
        self, form_submission_admin: FormSubmissionAdmin
    ) -> None:
        """
        Test that the list_filter attribute is defined and non-empty.

        Args:
            form_submission_admin (FormSubmissionAdmin): The admin class instance being tested.

        Asserts:
        --------
            list_filter is a tuple or list and has at least one item.
        """
        assert isinstance(form_submission_admin.list_filter, (tuple, list))
        assert len(form_submission_admin.list_filter) > 0

    def test_search_fields_configured(
        self, form_submission_admin: FormSubmissionAdmin
    ) -> None:
        """
        Test that the search_fields attribute is defined and non-empty.

        Args:
            form_submission_admin (FormSubmissionAdmin): The admin class instance being tested.

        Asserts:
        --------
            search_fields is a tuple or list and has at least one item.
        """
        assert isinstance(form_submission_admin.search_fields, (tuple, list))
        assert len(form_submission_admin.search_fields) > 0

    def test_admin_permissions(
        self, form_submission_admin: FormSubmissionAdmin, mock_request: HttpRequest
    ):
        """
        Test that admin permissions reflect the overridden settings and config.

        Args:
            form_submission_admin (FormSubmissionAdmin): The admin class instance being tested.
            mock_request (HttpRequest): A mock request object for permission checks.

        Asserts:
        --------
            - has_add_permission and has_change_permission are always False (overridden).
            - has_delete_permission and has_module_permission reflect config settings.
        """
        # Test with config permissions denied
        config.admin_has_add_permission = True  # Should be ignored due to override
        config.admin_has_change_permission = True  # Should be ignored due to override
        config.admin_has_delete_permission = False
        config.admin_has_module_permission = False
        assert (
            form_submission_admin.has_add_permission(mock_request) is False
        )  # Overridden
        assert (
            form_submission_admin.has_change_permission(mock_request) is False
        )  # Overridden
        assert form_submission_admin.has_delete_permission(mock_request) is False
        assert form_submission_admin.has_module_permission(mock_request) is False

        # Test with config permissions granted
        config.admin_has_add_permission = False  # Still False due to override
        config.admin_has_change_permission = False  # Still False due to override
        config.admin_has_delete_permission = True
        config.admin_has_module_permission = True
        assert (
            form_submission_admin.has_add_permission(mock_request) is False
        )  # Overridden
        assert (
            form_submission_admin.has_change_permission(mock_request) is False
        )  # Overridden
        assert form_submission_admin.has_delete_permission(mock_request) is True
        assert form_submission_admin.has_module_permission(mock_request) is True

    def test_readonly_fields(self, form_submission_admin: FormSubmissionAdmin) -> None:
        """
        Test that readonly_fields are properly configured.

        Args:
            form_submission_admin (FormSubmissionAdmin): The admin class instance being tested.

        Asserts:
        --------
            readonly_fields includes expected fields.
        """
        expected_fields = {"user", "submitted_at", "submitted_data"}
        assert isinstance(form_submission_admin.readonly_fields, (tuple, list))
        assert set(form_submission_admin.readonly_fields) == expected_fields

    def test_list_display_links(
        self, form_submission_admin: FormSubmissionAdmin
    ) -> None:
        """
        Test that list_display_links is properly configured.

        Args:
            form_submission_admin (FormSubmissionAdmin): The admin class instance being tested.

        Asserts:
        --------
            list_display_links matches the expected fields.
        """
        expected_links = {"id", "user"}
        assert isinstance(form_submission_admin.list_display_links, (tuple, list))
        assert set(form_submission_admin.list_display_links) == expected_links
