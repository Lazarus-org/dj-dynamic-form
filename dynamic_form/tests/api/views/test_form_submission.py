import sys

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from dynamic_form.models import FormSubmission, DynamicForm, DynamicField
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


class TestFormSubmissionViewSet:
    """
    Tests for the FormSubmissionViewSet API endpoints.

    This test class verifies the behavior of the FormSubmissionViewSet,
    ensuring that the list, retrieve, create, update, and destroy methods function correctly
    under various configurations and user permissions, including serializer validation.

    Tests:
    -------
    - test_list_form_submission: Verifies the list endpoint returns 200 OK and includes results when allowed.
    - test_retrieve_form_submission: Checks the retrieve endpoint returns 200 OK and correct data when allowed.
    - test_create_form_submission: Tests the create endpoint returns 201 Created with valid data when allowed.
    - test_update_form_submission: Tests the update endpoint returns 200 OK when allowed.
    - test_destroy_form_submission: Tests the destroy endpoint returns 204 No Content when allowed.
    - test_list_form_submission_disabled: Tests the list endpoint returns 405 when disabled.
    - test_retrieve_form_submission_disabled: Tests the retrieve endpoint returns 405 when disabled.
    - test_create_form_submission_invalid_data: Tests validation failure for missing required fields.
    - test_create_form_submission_invalid_form: Tests validation failure for non-existent or inactive form.
    """

    def test_list_form_submission(
        self,
        api_client: APIClient,
        form_submission: FormSubmission,
    ):
        """
        Test the list endpoint for FormSubmission.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            form_submission (FormSubmission): A sample FormSubmission instance.

        Asserts:
            The response status code is 200.
            The response data contains a 'results' key with the user's submissions.
        """
        api_client.force_authenticate(user=form_submission.user)

        config.api_form_submission_allow_list = True  # Enable list method
        config.api_form_submission_extra_permission_class = None

        url = reverse("form-submission-list")  # Adjust name based on your URLconf
        response = api_client.get(url)

        assert (
            response.status_code == 200
        ), f"Expected 200 OK, got {response.status_code}."
        assert "results" in response.data, "Expected 'results' in response data."
        assert len(response.data["results"]) > 0, "Expected data in the results."
        assert (
            response.data["results"][0]["id"] == form_submission.id
        ), f"Expected ID {form_submission.id}, got {response.data['results'][0]['id']}"

    def test_list_form_submission_anonymous(
        self,
        api_client: APIClient,
        form_submission: FormSubmission,
    ):
        """
        Test the list endpoint for FormSubmission with anonymous user.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            form_submission (FormSubmission): A sample FormSubmission instance.

        Asserts:
            The response status code is 200.
            The response data contains a 'results' key with the user's submissions.
        """
        config.api_form_submission_allow_list = True  # Enable list method
        config.api_form_submission_extra_permission_class = None

        url = reverse("form-submission-list")  # Adjust name based on your URLconf
        response = api_client.get(url)

        assert (
            response.status_code == 200
        ), f"Expected 200 OK, got {response.status_code}."
        assert "results" in response.data, "Expected 'results' in response data."
        assert len(response.data["results"]) == 0, "Expected no data in the results."

    def test_retrieve_form_submission(
        self,
        api_client: APIClient,
        form_submission: FormSubmission,
    ):
        """
        Test the retrieve endpoint for FormSubmission.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            form_submission (FormSubmission): The FormSubmission instance to retrieve.

        Asserts:
            The response status code is 200.
            The response data contains the correct FormSubmission ID and data.
        """
        api_client.force_authenticate(user=form_submission.user)

        config.api_form_submission_allow_retrieve = True  # Enable retrieve method

        url = reverse("form-submission-detail", kwargs={"pk": form_submission.pk})
        response = api_client.get(url)

        assert (
            response.status_code == 200
        ), f"Expected 200 OK, got {response.status_code}."
        assert (
            response.data["id"] == form_submission.id
        ), f"Expected ID {form_submission.id}, got {response.data['id']}."
        assert (
            response.data["submitted_data"] == form_submission.submitted_data
        ), f"Expected submitted data {form_submission.submitted_data}, got {response.data['submitted_data']}."

    def test_create_form_submission(
        self,
        api_client: APIClient,
        dynamic_form: DynamicForm,
        dynamic_field: DynamicField,
        user: User,
    ):
        """
        Test the create endpoint for FormSubmission.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_form (DynamicForm): The form to submit against.
            dynamic_field (DynamicField): A required field in the form.
            user (User): The user submitting the form.

        Asserts:
            The response status code is 201.
            The created submission has the correct data and user.
        """
        api_client.force_authenticate(user=user)

        config.api_form_submission_allow_create = True  # Enable create method

        url = reverse("form-submission-list")
        payload = {
            "form_id": dynamic_form.id,
            "submitted_data": {
                "email": "new@example.com"
            },  # Matches dynamic_field.name
        }
        response = api_client.post(url, payload, format="json")

        assert (
            response.status_code == 201
        ), f"Expected 201 Created, got {response.status_code}."
        assert (
            response.data["submitted_data"] == payload["submitted_data"]
        ), f"Expected submitted data {payload['submitted_data']}, got {response.data['submitted_data']}."
        assert (
            response.data["user"]["username"] == user.username
        ), "Expected user to be set from request."

    def test_update_form_submission(
        self,
        api_client: APIClient,
        form_submission: FormSubmission,
    ):
        """
        Test the update endpoint for FormSubmission.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            form_submission (FormSubmission): The FormSubmission instance to update.

        Asserts:
            The response status code is 200.
            The updated submission reflects the new data.
        """
        api_client.force_authenticate(user=form_submission.user)

        config.api_form_submission_allow_update = True  # Enable update method

        url = reverse("form-submission-detail", kwargs={"pk": form_submission.pk})
        payload = {"submitted_data": {"email": "updated@example.com"}}
        response = api_client.patch(url, payload, format="json")

        assert (
            response.status_code == 200
        ), f"Expected 200 OK, got {response.status_code}."
        assert (
            response.data["submitted_data"] == payload["submitted_data"]
        ), f"Expected submitted data {payload['submitted_data']}, got {response.data['submitted_data']}."

    def test_destroy_form_submission(
        self,
        api_client: APIClient,
        form_submission: FormSubmission,
    ):
        """
        Test the destroy endpoint for FormSubmission.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            form_submission (FormSubmission): The FormSubmission instance to delete.

        Asserts:
            The response status code is 204.
            The submission is removed from the database.
        """
        api_client.force_authenticate(user=form_submission.user)

        config.api_form_submission_allow_delete = True  # Enable destroy method

        url = reverse("form-submission-detail", kwargs={"pk": form_submission.pk})
        response = api_client.delete(url)

        assert (
            response.status_code == 204
        ), f"Expected 204 No Content, got {response.status_code}."
        assert not FormSubmission.objects.filter(
            pk=form_submission.pk
        ).exists(), "Submission was not deleted."

    def test_list_form_submission_disabled(
        self,
        api_client: APIClient,
        user: User,
        form_submission: FormSubmission,
    ):
        """
        Test the list view when disabled via configuration.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            user (User): A regular user for testing permissions.
            form_submission (FormSubmission): A sample FormSubmission instance.

        Asserts:
            The response status code is 405.
        """
        api_client.force_authenticate(user=user)

        config.api_form_submission_allow_list = False  # Disable list method

        url = reverse("form-submission-list")
        response = api_client.get(url)

        assert (
            response.status_code == 405
        ), f"Expected 405 Method Not Allowed, got {response.status_code}."

    def test_retrieve_form_submission_disabled(
        self,
        api_client: APIClient,
        admin_user: User,
        form_submission: FormSubmission,
    ):
        """
        Test the retrieve view when disabled via configuration.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            admin_user (User): The admin user for authentication.
            form_submission (FormSubmission): The FormSubmission instance to retrieve.

        Asserts:
            The response status code is 405.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_form_submission_allow_retrieve = False  # Disable retrieve method

        url = reverse("form-submission-detail", kwargs={"pk": form_submission.pk})
        response = api_client.get(url)

        assert (
            response.status_code == 405
        ), f"Expected 405 Method Not Allowed, got {response.status_code}."

    def test_create_form_submission_empty_data(
        self,
        api_client: APIClient,
        dynamic_form: DynamicForm,
        dynamic_field: DynamicField,
        user: User,
    ):
        """
        Test the create endpoint with empty data (empty submitted_data field).

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_form (DynamicForm): The form to submit against.
            dynamic_field (DynamicField): A required field in the form.
            user (User): The user submitting the form.

        Asserts:
            The response status code is 400.
            The error message indicates an empty required field.
        """
        api_client.force_authenticate(user=user)

        config.api_form_submission_allow_create = True  # Enable create method

        url = reverse("form-submission-list")
        payload = {"form_id": dynamic_form.id, "submitted_data": {}}
        response = api_client.post(url, payload, format="json")

        assert (
            response.status_code == 400
        ), f"Expected 400 Bad Request, got {response.status_code}."
        assert (
            "submitted_data" in response.data
        ), "Expected error empty 'submitted_data' field."

    def test_create_form_submission_invalid_data(
        self,
        api_client: APIClient,
        dynamic_form: DynamicForm,
        dynamic_field: DynamicField,
        user: User,
    ):
        """
        Test the create endpoint with invalid data (missing required field).

        Args:
            api_client (APIClient): The API client used to simulate requests.
            dynamic_form (DynamicForm): The form to submit against.
            dynamic_field (DynamicField): A required field in the form.
            user (User): The user submitting the form.

        Asserts:
            The response status code is 400.
            The error message indicates a missing required field.
        """
        api_client.force_authenticate(user=user)

        config.api_form_submission_allow_create = True  # Enable create method

        url = reverse("form-submission-list")
        payload = {
            "form_id": dynamic_form.id,
            "submitted_data": {"invalid": "data"},  # Missing required 'email' field
        }
        response = api_client.post(url, payload, format="json")

        assert (
            response.status_code == 400
        ), f"Expected 400 Bad Request, got {response.status_code}."
        assert "email" in response.data, "Expected error for missing 'email' field."

    def test_create_form_submission_invalid_form(
        self,
        api_client: APIClient,
        user: User,
    ):
        """
        Test the create endpoint with an invalid or inactive form.

        Args:
            api_client (APIClient): The API client used to simulate requests.
            user (User): The user submitting the form.

        Asserts:
            The response status code is 400.
            The error message indicates an invalid form ID.
        """
        api_client.force_authenticate(user=user)

        config.api_form_submission_allow_create = True  # Enable create method

        url = reverse("form-submission-list")
        payload = {
            "form_id": 999,  # Non-existent form ID
            "submitted_data": {"email": "test@example.com"},
        }
        response = api_client.post(url, payload, format="json")

        assert (
            response.status_code == 400
        ), f"Expected 400 Bad Request, got {response.status_code}."
        assert "form_id" in response.data, "Expected error for invalid form ID."
