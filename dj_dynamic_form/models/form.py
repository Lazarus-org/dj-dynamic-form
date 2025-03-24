from django.db.models import Model, CharField, DateTimeField, BooleanField, TextField
from django.utils.translation import gettext_lazy as _


class DynamicForm(Model):
    """
    A configurable form that can be created dynamically with custom fields.

    This model serves as the container for a form definition, storing metadata about
    the form such as its name, description, and active status. The actual fields
    of the form are defined in the related DynamicField model.

    Attributes:
        name (str): Unique identifier name for the form
        description (str, optional): Detailed explanation of the form's purpose
        is_active (bool): Toggles whether the form is available for submissions
        created_at (datetime): Auto-generated creation timestamp
        updated_at (datetime): Auto-generated last modification timestamp
    """

    name = CharField(
        _("Form Name"),
        unique=True,
        max_length=255,
        help_text=_("The name of the form."),
        db_comment="A unique name for identifying the form.",
    )
    description = TextField(
        _("Description"),
        blank=True,
        null=True,
        help_text=_("Optional description of the form."),
        db_comment="A short description about the form's purpose.",
    )
    is_active = BooleanField(
        _("Active Status"),
        default=True,
        help_text=_("Whether this form is currently active and accepting submissions."),
        db_comment="Controls if the form is available for use.",
    )
    created_at = DateTimeField(
        _("Creation Date"),
        auto_now_add=True,
        help_text=_("Timestamp when the form was created."),
        db_comment="The date and time when the form was first created.",
    )
    updated_at = DateTimeField(
        _("Last Updated"),
        auto_now=True,
        help_text=_("Timestamp when the form was last updated."),
        db_comment="The date and time of the last modification.",
    )

    class Meta:
        verbose_name = _("Dynamic Form")
        verbose_name_plural = _("Dynamic Forms")
        db_table = "dynamic_forms"
        ordering = ["name"]

    def __str__(self):
        return self.name
