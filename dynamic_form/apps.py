from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjDynamicFormConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dynamic_form"
    verbose_name = _("Django Dynamic Form")
