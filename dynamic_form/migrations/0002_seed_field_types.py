from django.db import migrations
from django.utils.translation import gettext_lazy as _


def forwards_func(apps, schema_editor):
    """
    Populate the FieldType table with default values from the original enum.
    """
    FieldType = apps.get_model("dynamic_form", "FieldType")
    default_field_types = [
        {
            "name": "text",
            "label": _("Text Field"),
            "description": _("A single-line text input."),
        },
        {
            "name": "number",
            "label": _("Number Field"),
            "description": _("A numeric input."),
        },
        {
            "name": "email",
            "label": _("Email Field"),
            "description": _("An email address input."),
        },
        {
            "name": "boolean",
            "label": _("Boolean Field"),
            "description": _("A true/false checkbox."),
        },
        {
            "name": "date",
            "label": _("Date Field"),
            "description": _("A date picker input."),
        },
        {
            "name": "dropdown",
            "label": _("Dropdown Field"),
            "description": _("A selectable list of options."),
        },
        {
            "name": "textarea",
            "label": _("Textarea Field"),
            "description": _("A multi-line text input."),
        },
        {
            "name": "checkbox",
            "label": _("Checkbox Field"),
            "description": _("A checkbox input."),
        },
        {
            "name": "radio",
            "label": _("Radio Field"),
            "description": _("A set of radio buttons for selection."),
        },
        {
            "name": "file",
            "label": _("File Field"),
            "description": _("An input for file uploads."),
        },
    ]

    db_alias = schema_editor.connection.alias
    for field_type in default_field_types:
        # Only create if it doesn't exist to avoid duplicates on re-runs
        FieldType.objects.using(db_alias).get_or_create(
            name=field_type["name"],
            defaults={
                "label": field_type["label"],
                "description": field_type["description"],
                "is_active": True,
            },
        )


class Migration(migrations.Migration):
    dependencies = [
        ("dynamic_form", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
