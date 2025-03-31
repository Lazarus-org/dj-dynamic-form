from django.conf import settings
from django.db.models import (
    CASCADE,
    SET_NULL,
    DateTimeField,
    ForeignKey,
    Index,
    JSONField,
    Model,
)
from django.utils.translation import gettext_lazy as _


class FormSubmission(Model):
    """Records a user's submission of data to a dynamic form.

    This model stores the actual data submitted by users for each DynamicForm instance,
    along with metadata about the submission. The submitted data is stored as JSON
    to accommodate the variable structure of different form configurations.

    Attributes:
        user (User, optional): Authenticated user who made the submission
        form (DynamicForm): Reference to the submitted form definition
        submitted_data (JSON): Structured data containing all field responses
        submitted_at (datetime): Timestamp of when the submission occurred

    """

    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Submitting User"),
        on_delete=SET_NULL,
        blank=True,
        null=True,
        help_text=_("The user who submitted this form, if authenticated."),
        db_comment="Optional reference to the submitting user.",
    )
    form = ForeignKey(
        "DynamicForm",
        verbose_name=_("Submitted Form"),
        on_delete=CASCADE,
        help_text=_("The form to which this submission belongs."),
        db_comment="A foreign key linking this submission to a dynamic form.",
    )
    submitted_data = JSONField(
        _("Submission Data"),
        help_text=_("The data submitted by the user."),
        db_comment="Stores user responses in a JSON format.",
    )
    submitted_at = DateTimeField(
        _("Submission Time"),
        auto_now_add=True,
        help_text=_("Timestamp when the submission was made."),
        db_comment="The date and time when this form was submitted.",
    )

    class Meta:
        verbose_name = _("Form Submission")
        verbose_name_plural = _("Form Submissions")
        db_table = "form_submissions"
        ordering = ["-submitted_at"]
        indexes = [
            Index(fields=["form", "submitted_at"]),
            Index(fields=["user", "submitted_at"]),
        ]

    def __str__(self):
        return f"Submission #{self.id} for Form #{self.form_id} at {self.submitted_at}"
