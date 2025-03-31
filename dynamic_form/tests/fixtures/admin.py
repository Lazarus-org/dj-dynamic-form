import pytest
from django.contrib.admin import AdminSite
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import RequestFactory


from dynamic_form.admin import DynamicFormAdmin, FormSubmissionAdmin
from dynamic_form.models import DynamicForm, FormSubmission


@pytest.fixture
def request_factory() -> RequestFactory:
    """
    Fixture to provide an instance of RequestFactory.

    Returns:
    -------
        RequestFactory: An instance of Django's RequestFactory.
    """
    return RequestFactory()


@pytest.fixture
def mock_request():
    """
    Fixture to provide a mock HttpRequest object with messages support.

    Returns:
        HttpRequest: A Django HttpRequest object with messages middleware support.
    """
    request = RequestFactory().get("/")
    setattr(request, "session", "session")
    messages_storage = FallbackStorage(request)
    setattr(request, "_messages", messages_storage)
    return request


@pytest.fixture
def admin_site() -> AdminSite:
    """
    Fixture to provide an instance of AdminSite.

    Returns:
    -------
        AdminSite: An instance of Django's AdminSite.
    """
    return AdminSite()


@pytest.fixture
def dynamic_form_admin(admin_site: AdminSite) -> DynamicFormAdmin:
    """
    Fixture to provide an instance of DynamicFormAdmin.

    Args:
    ----
        admin_site (AdminSite): An instance of Django's AdminSite.

    Returns:
    -------
        DynamicFormAdmin: An instance of DynamicFormAdmin.
    """
    return DynamicFormAdmin(DynamicForm, admin_site)


@pytest.fixture
def form_submission_admin(admin_site: AdminSite) -> FormSubmissionAdmin:
    """
    Fixture to provide an instance of FormSubmissionAdmin.

    Args:
    ----
        admin_site (AdminSite): An instance of Django's AdminSite.

    Returns:
    -------
        FormSubmissionAdmin: An instance of the admin class.
    """
    return FormSubmissionAdmin(FormSubmission, admin_site)
