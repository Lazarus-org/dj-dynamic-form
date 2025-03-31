import sys

import pytest

from dynamic_form.models import FieldType
from dynamic_form.tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.models,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


@pytest.mark.django_db
class TestFieldTypeModel:
    """
    Test suite for the FieldType model.
    """

    def test_str_method(self, field_type: FieldType) -> None:
        """
        Test that the __str__ method returns the correct string representation of a Field Type.

        Asserts:
        -------
            - The string representation includes the correct structure.
        """
        expected_str = field_type.label
        assert (
            str(field_type) == expected_str
        ), f"Expected the __str__ method to return '{expected_str}', but got '{str(field_type)}'."
