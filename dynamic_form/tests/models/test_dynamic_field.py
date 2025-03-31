import sys

import pytest

from dynamic_form.models import DynamicField
from dynamic_form.tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.models,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


@pytest.mark.django_db
class TestDynamicFieldModel:
    """
    Test suite for the DynamicField model.
    """

    def test_str_method(self, dynamic_field: DynamicField) -> None:
        """
        Test that the __str__ method returns the correct string representation of a Dynamic Field.

        Asserts:
        -------
            - The string representation includes the correct structure.
        """
        expected_str = f"{dynamic_field.name}- Form #{dynamic_field.form_id}"
        assert (
            str(dynamic_field) == expected_str
        ), f"Expected the __str__ method to return '{expected_str}', but got '{str(dynamic_field)}'."

        assert dynamic_field.get_label() == dynamic_field.label or dynamic_field.name
