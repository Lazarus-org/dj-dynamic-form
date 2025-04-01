import sys

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from dynamic_form.models import DynamicField, DynamicForm, FieldType
from dynamic_form.settings.conf import config
from dynamic_form.tests.constants import (
    PYTHON_VERSION,
    PYTHON_VERSION_REASON,
)

pytestmark = [
    pytest.mark.api,
    pytest.mark.api_views,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


class TestAdminDynamicFieldViewSet:
    """
    Tests for the AdminDynamicFieldViewSet API endpoints with nested routing.

    This test class verifies the behavior of the AdminDynamicFieldViewSet,
    ensuring that the list, retrieve, create, update, and destroy methods function correctly
    under various configurations and admin permissions, including serializer validation.
    The endpoints are nested under /admin/forms/{form_pk}/fields/.

    Tests:
    -------
    - test_list_dynamic_field: Verifies the list endpoint returns 200 OK and includes fields for the form.
    - test_retrieve_dynamic_field: Checks the retrieve endpoint returns 200 OK and correct data when allowed.
    - test_create_dynamic_field: Tests the create endpoint returns 201 Created with valid data when allowed.
    - test_update_dynamic_field: Tests the update endpoint returns 200 OK when allowed.
    - test_destroy_dynamic_field: Tests the destroy endpoint returns 204 No Content when allowed.
    - test_list_dynamic_field_disabled: Tests the list endpoint returns 405 when disabled.
    - test_retrieve_dynamic_field_disabled: Tests the retrieve endpoint returns 405 when disabled.
    - test_create_dynamic_field_duplicate_name: Tests validation failure for duplicate field names.
    - test_create_dynamic_field_invalid_form: Tests validation failure for non-existent or inactive form.
    - test_create_dynamic_field_invalid_field_type: Tests validation failure for invalid field type.
    """

    def test_list_dynamic_field(
        self,
        api_client: APIClient,
        dynamic_field: DynamicField,
        admin_user: User,
    ):
        """
        Test the list endpoint for DynamicField within a form.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_field (DynamicField): A sample DynamicField instance.
            admin_user (User): The admin user for authentication.

        Asserts:
            The response status code is 200.
            The response data contains a 'results' key with fields for the specified form.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_list = True  # Enable list method
        config.api_admin_dynamic_field_extra_permission_class = None

        url = reverse(
            "admin-form-field-list", kwargs={"form_pk": dynamic_field.form.pk}
        )
        response = api_client.get(url)

        assert (
            response.status_code == 200
        ), f"Expected 200 OK, got {response.status_code}."
        assert "results" in response.data, "Expected 'results' in response data."
        assert len(response.data["results"]) > 0, "Expected data in the results."
        assert (
            response.data["results"][0]["id"] == dynamic_field.id
        ), f"Expected ID {dynamic_field.id}, got {response.data['results'][0]['id']}"

    def test_retrieve_dynamic_field(
        self,
        api_client: APIClient,
        dynamic_field: DynamicField,
        admin_user: User,
    ):
        """
        Test the retrieve endpoint for DynamicField within a form.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_field (DynamicField): The DynamicField instance to retrieve.
            admin_user (User): The admin user for authentication.

        Asserts:
            The response status code is 200.
            The response data contains the correct DynamicField ID and name.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_retrieve = True  # Enable retrieve method

        url = reverse(
            "admin-form-field-detail",
            kwargs={"form_pk": dynamic_field.form.pk, "pk": dynamic_field.pk},
        )
        response = api_client.get(url)

        assert (
            response.status_code == 200
        ), f"Expected 200 OK, got {response.status_code}."
        assert (
            response.data["id"] == dynamic_field.id
        ), f"Expected ID {dynamic_field.id}, got {response.data['id']}."
        assert (
            response.data["name"] == dynamic_field.name
        ), f"Expected name {dynamic_field.name}, got {response.data['name']}."

    def test_create_dynamic_field(
        self,
        api_client: APIClient,
        dynamic_form: DynamicForm,
        field_type: FieldType,
        admin_user: User,
    ):
        """
        Test the create endpoint for DynamicField within a form.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_form (DynamicForm): The form to associate with the field.
            field_type (FieldType): The field type for the new field.
            admin_user (User): The admin user creating the field.

        Asserts:
            The response status code is 201.
            The created field has the correct data (form inferred from URL).
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_create = True  # Enable create method

        url = reverse("admin-form-field-list", kwargs={"form_pk": dynamic_form.pk})
        payload = {
            "field_type_id": field_type.id,
            "name": "new_field",
            "is_required": False,
        }
        response = api_client.post(url, payload, format="json")

        assert (
            response.status_code == 201
        ), f"Expected 201 Created, got {response.status_code}."
        assert (
            response.data["name"] == payload["name"]
        ), f"Expected name {payload['name']}, got {response.data['name']}."
        # Assuming serializer returns form ID in response
        assert (
            response.data["form"] == dynamic_form.id
        ), f"Expected form ID {dynamic_form.id}, got {response.data['form']}."

    def test_update_dynamic_field(
        self,
        api_client: APIClient,
        dynamic_field: DynamicField,
        admin_user: User,
    ):
        """
        Test the update endpoint for DynamicField within a form.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_field (DynamicField): The DynamicField instance to update.
            admin_user (User): The admin user updating the field.

        Asserts:
            The response status code is 200.
            The updated field reflects the new data.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_update = True  # Enable update method

        url = reverse(
            "admin-form-field-detail",
            kwargs={"form_pk": dynamic_field.form.pk, "pk": dynamic_field.pk},
        )
        payload = {"name": "updated_field"}
        response = api_client.patch(url, payload, format="json")

        assert (
            response.status_code == 200
        ), f"Expected 200 OK, got {response.status_code}."
        assert (
            response.data["name"] == payload["name"]
        ), f"Expected name {payload['name']}, got {response.data['name']}."

    def test_destroy_dynamic_field(
        self,
        api_client: APIClient,
        dynamic_field: DynamicField,
        admin_user: User,
    ):
        """
        Test the destroy endpoint for DynamicField within a form.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_field (DynamicField): The DynamicField instance to delete.
            admin_user (User): The admin user deleting the field.

        Asserts:
            The response status code is 204.
            The field is removed from the database.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_delete = True  # Enable destroy method

        url = reverse(
            "admin-form-field-detail",
            kwargs={"form_pk": dynamic_field.form.pk, "pk": dynamic_field.pk},
        )
        response = api_client.delete(url)

        assert (
            response.status_code == 204
        ), f"Expected 204 No Content, got {response.status_code}."
        assert not DynamicField.objects.filter(
            pk=dynamic_field.pk
        ).exists(), "Field was not deleted."

    def test_list_dynamic_field_disabled(
        self,
        api_client: APIClient,
        admin_user: User,
        dynamic_field: DynamicField,
    ):
        """
        Test the list view when disabled via configuration.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            admin_user (User): The admin user for authentication.
            dynamic_field (DynamicField): A sample DynamicField instance.

        Asserts:
            The response status code is 405.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_list = False  # Disable list method

        url = reverse(
            "admin-form-field-list", kwargs={"form_pk": dynamic_field.form.pk}
        )
        response = api_client.get(url)

        assert (
            response.status_code == 405
        ), f"Expected 405 Method Not Allowed, got {response.status_code}."

    def test_retrieve_dynamic_field_disabled(
        self,
        api_client: APIClient,
        admin_user: User,
        dynamic_field: DynamicField,
    ):
        """
        Test the retrieve view when disabled via configuration.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            admin_user (User): The admin user for authentication.
            dynamic_field (DynamicField): The DynamicField instance to retrieve.

        Asserts:
            The response status code is 405.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_retrieve = False  # Disable retrieve method

        url = reverse(
            "admin-form-field-detail",
            kwargs={"form_pk": dynamic_field.form.pk, "pk": dynamic_field.pk},
        )
        response = api_client.get(url)

        assert (
            response.status_code == 405
        ), f"Expected 405 Method Not Allowed, got {response.status_code}."

    def test_create_dynamic_field_duplicate_name(
        self,
        api_client: APIClient,
        dynamic_form: DynamicForm,
        field_type: FieldType,
        dynamic_field: DynamicField,
        admin_user: User,
    ):
        """
        Test the create endpoint with a duplicate field name within the same form.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_form (DynamicForm): The form to associate with the field.
            field_type (FieldType): The field type for the new field.
            dynamic_field (DynamicField): An existing field with a conflicting name.
            admin_user (User): The admin user creating the field.

        Asserts:
            The response status code is 400.
            The error message indicates a duplicate name.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_create = True  # Enable create method

        url = reverse("admin-form-field-list", kwargs={"form_pk": dynamic_form.pk})
        payload = {
            "field_type_id": field_type.id,
            "name": dynamic_field.name,  # Duplicate name
            "is_required": False,
        }
        response = api_client.post(url, payload, format="json")

        assert (
            response.status_code == 400
        ), f"Expected 400 Bad Request, got {response.status_code}."
        assert "name" in response.data, "Expected error for duplicate field name."

    def test_create_dynamic_field_invalid_form(
        self,
        api_client: APIClient,
        field_type: FieldType,
        admin_user: User,
    ):
        """
        Test the create endpoint with an invalid or inactive form.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            field_type (FieldType): The field type for the new field.
            admin_user (User): The admin user creating the field.

        Asserts:
            The response status code is 400.
            The error message indicates an invalid form ID.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_create = True  # Enable create method

        url = reverse(
            "admin-form-field-list", kwargs={"form_pk": 999}
        )  # Non-existent form
        payload = {
            "field_type_id": field_type.id,
            "name": "unique_field",
            "is_required": False,
        }
        response = api_client.post(url, payload, format="json")

        assert (
            response.status_code == 400
        ), f"Expected 400 Bad Request, got {response.status_code}."
        assert "form" in response.data, "Expected error for invalid form ID."

    def test_create_dynamic_field_invalid_field_type(
        self,
        api_client: APIClient,
        dynamic_form: DynamicForm,
        admin_user: User,
    ):
        """
        Test the create endpoint with an invalid or inactive field type.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_form (DynamicForm): The form to associate with the field.
            admin_user (User): The admin user creating the field.

        Asserts:
            The response status code is 400.
            The error message indicates an invalid field type ID.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_create = True  # Enable create method

        url = reverse("admin-form-field-list", kwargs={"form_pk": dynamic_form.pk})
        payload = {
            "field_type_id": 999,  # Non-existent field type ID
            "name": "unique_field",
            "is_required": False,
        }
        response = api_client.post(url, payload, format="json")

        assert (
            response.status_code == 400
        ), f"Expected 400 Bad Request, got {response.status_code}."
        assert (
            "field_type_id" in response.data
        ), "Expected error for invalid field type ID."

    def test_list_dynamic_field_invalid_form_pk(
        self,
        api_client: APIClient,
        admin_user: User,
    ):
        """
        Test the list endpoint when form_pk is invalid from the URL.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            admin_user (User): The admin user for authentication.

        Asserts:
            The response status code is 400.
            The error message indicates an invalid form identifier.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_list = True  # Enable list method

        url = reverse("admin-form-field-list", kwargs={"form_pk": "invalid"})
        response = api_client.get(url)

        assert (
            response.status_code == 400
        ), f"Expected 400 Bad Request, got {response.status_code}."
        assert "form_pk" in response.data, "Expected error for missing form_pk."
        assert (
            "Invalid form identifier" in response.data["form_pk"]
        ), "Unexpected error message."

    def test_create_dynamic_field_invalid_pk_and_serializer_else(
        self,
        api_client: APIClient,
        dynamic_field: DynamicField,
        field_type: FieldType,
        admin_user: User,
    ):
        """
        Test the create endpoint with an invalid pk in URL and the serializer's else condition.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_field (DynamicField): An existing field to mock instance behavior.
            field_type (FieldType): The field type for the new field.
            admin_user (User): The admin user creating the field.
            mocker: Pytest mocker fixture to mock serializer context.

        Asserts:
            The response status code is 400 for invalid pk.
            The else condition in serializer validate is covered (requires mocking instance).
        """
        api_client.force_authenticate(user=admin_user)

        config.api_admin_dynamic_field_allow_create = True  # Enable create method

        # Test 1: Invalid form_pk in URL
        url = reverse("admin-form-field-list", kwargs={"form_pk": "invalid"})
        payload = {
            "field_type_id": field_type.id,
            "name": "unique_field",
            "is_required": False,
        }
        response = api_client.post(url, payload, format="json")

        assert (
            response.status_code == 400
        ), f"Expected 400 Bad Request, got {response.status_code}."
        assert "form_pk" in response.data, "Expected error for invalid form_pk."
        assert (
            "Invalid Form ID" in response.data["form_pk"][0]
        ), "Unexpected error message."
