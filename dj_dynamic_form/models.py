from django.db import models
from django.utils.translation import gettext_lazy as _

class DynamicForm(models.Model):
    """
    Model representing a dynamically created form.
    """
    name = models.CharField(
        max_length=255,
        help_text=_("The name of the form."),
        db_comment="A unique name for identifying the form."
    )
    description = models.TextField(
        blank=True, null=True,
        help_text=_("Optional description of the form."),
        db_comment="A short description about the form's purpose."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Timestamp when the form was created."),
        db_comment="The date and time when the form was first created."
    )

    class Meta:
        verbose_name = _("Dynamic Form")
        verbose_name_plural = _("Dynamic Forms")

    def __str__(self):
        return self.name




class DynamicField(models.Model):
    """
    Represents a field within a dynamic form.
    """
    FORM_FIELD_TYPES = [
        ("text", _("Text Field")),
        ("number", _("Number Field")),
        ("email", _("Email Field")),
        ("boolean", _("Boolean Field")),
        ("date", _("Date Field")),
        ("dropdown", _("Dropdown Field")),
    ]

    form = models.ForeignKey(
        DynamicForm, on_delete=models.CASCADE,
        related_name="fields",
        help_text=_("The form to which this field belongs."),
        db_comment="A foreign key linking this field to its parent form."
    )
    name = models.CharField(
        max_length=255,
        help_text=_("The name of the field."),
        db_comment="A unique identifier for the field inside a form."
    )
    field_type = models.CharField(
        max_length=20, choices=FORM_FIELD_TYPES,
        help_text=_("The type of field (e.g., text, number, dropdown, etc.)."),
        db_comment="Defines the type of input field."
    )
    is_required = models.BooleanField(
        default=False,
        help_text=_("Whether this field is required."),
        db_comment="If True, this field must be filled when submitting the form."
    )
    choices = models.JSONField(
        blank=True, null=True,
        help_text=_("Applicable only for dropdown fields, stores the choices available."),
        db_comment="A JSON field storing dropdown choices."
    )

    class Meta:
        verbose_name = _("Dynamic Field")
        verbose_name_plural = _("Dynamic Fields")

    def __str__(self):
        return f"{self.name}"
    

class FormSubmission(models.Model):
    """
    Stores responses submitted for a dynamic form.
    """
    form = models.ForeignKey(
        DynamicForm, on_delete=models.CASCADE,
        help_text=_("The form to which this submission belongs."),
        db_comment="A foreign key linking this submission to a dynamic form."
    )
    submitted_data = models.JSONField(
        help_text=_("The data submitted by the user."),
        db_comment="Stores user responses in a JSON format."
    )
    submitted_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Timestamp when the submission was made."),
        db_comment="The date and time when this form was submitted."
    )

    class Meta:
        verbose_name = _("Form Submission")
        verbose_name_plural = _("Form Submissions")

    def __str__(self):
        return f"Submission for {self.form.name} on {self.submitted_at}"
