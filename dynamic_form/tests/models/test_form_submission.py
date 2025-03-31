import sys

import pytest

from dynamic_form.models import FormSubmission
from dynamic_form.tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.models,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


@pytest.mark.django_db
class TestFormSubmissionModel:
    """
    Test suite for the FormSubmission model.
    """

    def test_str_method(self, form_submission: FormSubmission) -> None:
        """
        Test that the __str__ method returns the correct string representation of a FormSubmission.

        Asserts:
        -------
            - The string representation includes the correct structure.
        """
        expected_str = (
            f"Submission #{form_submission.id} for Form #{form_submission.form_id} "
            f"at {form_submission.submitted_at}"
        )
        assert (
            str(form_submission) == expected_str
        ), f"Expected the __str__ method to return '{expected_str}', but got '{str(form_submission)}'."
