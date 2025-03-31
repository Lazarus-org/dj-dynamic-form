import pytest
from django.contrib.auth import get_user_model
from dynamic_form.models import DynamicForm, DynamicField, FieldType, FormSubmission

User = get_user_model()


@pytest.fixture
def field_type(db) -> FieldType:
    """
    Fixture to create a FieldType instance.

    Creates a FieldType with a default name and description, useful for associating
    with DynamicField instances.

    Args:
        db: Pytest fixture to enable database access.

    Returns:
        FieldType: The created FieldType instance.
    """
    field_type = FieldType.objects.create(
        name="test",
        label="Test",
        description="A simple test field",
    )
    return field_type


@pytest.fixture
def dynamic_form(db, user) -> DynamicForm:
    """
    Fixture to create a DynamicForm instance.

    Creates a DynamicForm with default settings, marked as active.

    Args:
        db: Pytest fixture to enable database access.

    Returns:
        DynamicForm: The created DynamicForm instance.
    """
    return DynamicForm.objects.create(
        name="Test Form",
        is_active=True,
    )


@pytest.fixture
def dynamic_field(db, dynamic_form, field_type) -> DynamicField:
    """
    Fixture to create a DynamicField instance linked to a DynamicForm and FieldType.

    Creates a DynamicField with a unique name within the form, associated with the
    provided DynamicForm and FieldType.

    Args:
        db: Pytest fixture to enable database access.
        dynamic_form: The DynamicForm fixture to associate with the field.
        field_type: The FieldType fixture to define the field's type.

    Returns:
        DynamicField: The created DynamicField instance.
    """
    return DynamicField.objects.create(
        form=dynamic_form,
        field_type=field_type,
        name="email",
        is_required=True,
    )


@pytest.fixture
def form_submission(db, user, dynamic_form) -> FormSubmission:
    """
    Fixture to create a FormSubmission instance linked to a User and DynamicForm.

    Creates a FormSubmission with sample data, associated with the provided user
    and form.

    Args:
        db: Pytest fixture to enable database access.
        user: The user fixture to associate with the submission.
        dynamic_form: The DynamicForm fixture to associate with the submission.

    Returns:
        FormSubmission: The created FormSubmission instance.
    """
    return FormSubmission.objects.create(
        user=user,
        form=dynamic_form,
        submitted_data={"email": "test@example.com"},
    )
