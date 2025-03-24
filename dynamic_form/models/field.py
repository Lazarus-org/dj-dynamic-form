from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    JSONField,
    BooleanField,
    PositiveIntegerField,
    PROTECT,
)
from django.utils.translation import gettext_lazy as _


class DynamicField(Model):
    """
    Defines a single field within a dynamic form with configurable properties.

    This model represents all possible field types that can be added to a DynamicForm,
    with attributes controlling the field's behavior, validation, and presentation.

    Attributes:
        form (DynamicForm): Parent form this field belongs to
        name (str): Internal identifier for the field
        field_type (FieldType): Determines the field type this field belongs to (text, number, dropdown etc.)
        label (str, optional): Display label (defaults to name if not provided)
        is_required (bool): Whether the field must be filled
        choices (JSON, optional): Available options for dropdown/radio/checkbox fields
        default_value (JSON, optional): Initial value for the field
        validation_rules (JSON, optional): Custom validation constraints
        order (int): Position of the field in the form layout
    """

    form = ForeignKey(
        to="DynamicForm",
        verbose_name=_("Parent Form"),
        on_delete=CASCADE,
        related_name="fields",
        help_text=_("The form to which this field belongs."),
        db_comment="A foreign key linking this field to its parent form.",
    )
    name = CharField(
        _("Field Name"),
        max_length=255,
        help_text=_("The name of the field."),
        db_comment="A unique identifier for the field inside a form.",
    )
    field_type = ForeignKey(
        to="FieldType",
        on_delete=PROTECT,
        verbose_name=_("Field Type"),
        help_text=_(
            "The type of field (e.g., text, number, dropdown, etc.), linked to a FieldType entry."
        ),
        db_comment="References the field type definition.",
    )
    label = CharField(
        _("Display Label"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The display label for this field (defaults to name if blank)."),
        db_comment="User-friendly label for the field.",
    )
    is_required = BooleanField(
        _("Required Field"),
        default=False,
        help_text=_("Whether this field is required."),
        db_comment="If True, this field must be filled when submitting the form.",
    )
    choices = JSONField(
        _("Field Choices"),
        blank=True,
        null=True,
        help_text=_(
            "Applicable only for dropdown fields, stores the choices available."
        ),
        db_comment="A JSON field storing dropdown choices.",
    )
    default_value = JSONField(
        _("Default Value"),
        blank=True,
        null=True,
        help_text=_("Default value for this field, stored as JSON."),
        db_comment="The default value to prefill the field.",
    )
    validation_rules = JSONField(
        _("Validation Rules"),
        blank=True,
        null=True,
        help_text=_(
            "Optional validation rules (e.g., min_length, max_value, custom_validation)."
        ),
        db_comment="JSON storing validation constraints.",
    )
    order = PositiveIntegerField(
        _("Display Order"),
        default=0,
        help_text=_("Order in which this field appears in the form."),
        db_comment="Sorting order for field display.",
    )

    class Meta:
        verbose_name = _("Dynamic Field")
        verbose_name_plural = _("Dynamic Fields")
        db_table = "dynamic_form_fields"
        ordering = ["form", "order"]
        unique_together = ["form", "name"]

    def __str__(self):
        return f"{self.name}- Form #{self.form_id}"

    def get_label(self):
        """Returns the display label for the field, falling back to the name if no label is set."""
        return self.label or self.name
