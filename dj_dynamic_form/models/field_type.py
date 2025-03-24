from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    BooleanField,
    UniqueConstraint,
)
from django.utils.translation import gettext_lazy as _


class FieldType(Model):
    """
    Model representing a type of field that can be used in a dynamic form.

    This model replaces the static `FORM_FIELD_TYPES` enum, allowing field types to be
    defined dynamically in the database. It enables users to extend the system with custom
    field types (e.g., 'phone', 'multi_select') without modifying the package's codebase.
    Each field type can include metadata like a label and description, making it suitable
    for both backend validation and frontend rendering.

    Examples:
        - name: "text", label: "Text Field", description: "A single-line text input."
        - name: "dropdown", label: "Dropdown Field", description: "A selectable list."
    """

    name = CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Name"),
        help_text=_(
            "A short, unique identifier for this field type (e.g., 'text', 'number')."
        ),
        db_comment="Unique slug-like name for the field type, used as a key in forms.",
    )
    label = CharField(
        verbose_name=_("Display Label"),
        max_length=255,
        help_text=_("The human-readable name of this field type, displayed to users."),
        db_comment="User-friendly label for the field type (e.g., 'Text Field').",
    )
    description = TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_(
            "An optional description of this field type’s purpose or behavior."
        ),
        db_comment="Detailed explanation of the field type, useful for documentation.",
    )
    created_at = DateTimeField(
        auto_now_add=True,
        verbose_name=_("Creation Date"),
        help_text=_("Timestamp when this field type was created."),
        db_comment="The date and time when this field type was first added.",
    )
    is_active = BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Whether this field type is currently available for use in forms."),
        db_comment="Controls if the field type can be selected for new fields.",
    )

    class Meta:
        verbose_name = _("Field Type")
        verbose_name_plural = _("Field Types")
        ordering = ["name"]
        constraints = [UniqueConstraint(fields=["name"], name="unique_field_type_name")]

    def __str__(self):
        """
        Returns the human-readable label of the field type.

        Returns:
            str: The label of this field type (e.g., 'Text Field').
        """
        return self.label
