import sys

import pytest

from dynamic_form.models import DynamicForm
from dynamic_form.tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.models,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


@pytest.mark.django_db
class TestDynamicFormModel:
    """
    Test suite for the DynamicForm model.
    """

    def test_str_method(self, dynamic_form: DynamicForm) -> None:
        """
        Test that the __str__ method returns the correct string representation of a Dynamic Field.

        Asserts:
        -------
            - The string representation includes the correct structure.
        """
        expected_str = dynamic_form.name
        assert (
            str(dynamic_form) == expected_str
        ), f"Expected the __str__ method to return '{expected_str}', but got '{str(dynamic_form)}'."
