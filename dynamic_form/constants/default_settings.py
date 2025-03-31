from dataclasses import dataclass, field
from typing import List, Optional

from dynamic_form.utils.user_model import REQUIRED_FIELDS, USERNAME_FIELD


@dataclass(frozen=True)
class DefaultAdminSettings:
    admin_site_class: Optional[str] = None
    admin_has_add_permission: bool = True
    admin_has_change_permission: bool = True
    admin_has_delete_permission: bool = True
    admin_has_module_permission: bool = True


@dataclass(frozen=True)
class DefaultThrottleSettings:
    base_user_throttle_rate: str = "30/minute"
    staff_user_throttle_rate: str = "100/minute"
    throttle_class: str = "dynamic_form.api.throttlings.RoleBasedUserRateThrottle"


@dataclass(frozen=True)
class DefaultSerializerSettings:
    user_serializer_class: Optional[str] = None
    dynamic_form_serializer_class: Optional[str] = None
    dynamic_field_serializer_class: Optional[str] = None
    field_type_serializer_class: Optional[str] = None
    form_submission_serializer_class: Optional[str] = None
    user_serializer_fields: List[str] = field(
        default_factory=lambda: [USERNAME_FIELD] + list(REQUIRED_FIELDS)
    )


@dataclass(frozen=True)
class DefaultAPISettings:
    admin_permission_class: Optional[str] = "rest_framework.permissions.IsAdminUser"
    extra_permission_class: Optional[str] = None
    pagination_class: str = "dynamic_form.api.paginations.DefaultLimitOffSetPagination"
    parser_classes: List[str] = field(
        default_factory=lambda: [
            "rest_framework.parsers.JSONParser",
            "rest_framework.parsers.MultiPartParser",
            "rest_framework.parsers.FormParser",
        ]
    )


@dataclass(frozen=True)
class DefaultDynamicFormAPISettings:
    filterset_class: Optional[str] = None
    ordering_fields: List[str] = field(
        default_factory=lambda: ["created_at", "updated_at"]
    )
    search_fields: List[str] = field(default_factory=lambda: ["name", "description"])
    allow_list: bool = True
    allow_retrieve: bool = True
    admin_allow_list: bool = True
    admin_allow_retrieve: bool = True
    admin_allow_create: bool = True
    admin_allow_update: bool = True
    admin_allow_delete: bool = True


@dataclass(frozen=True)
class DefaultDynamicFieldAPISettings:
    filterset_class: Optional[str] = None
    ordering_fields: List[str] = field(default_factory=lambda: ["order"])
    search_fields: List[str] = field(default_factory=lambda: ["name", "label"])
    allow_list: bool = True
    allow_retrieve: bool = True
    admin_allow_list: bool = True
    admin_allow_retrieve: bool = True
    admin_allow_create: bool = True
    admin_allow_update: bool = True
    admin_allow_delete: bool = True


@dataclass(frozen=True)
class DefaultFieldTypeAPISettings:
    filterset_class: Optional[str] = None
    ordering_fields: List[str] = field(
        default_factory=lambda: ["created_at", "updated_at"]
    )
    search_fields: List[str] = field(
        default_factory=lambda: ["name", "label", "description"]
    )
    allow_list: bool = True
    allow_retrieve: bool = True
    admin_allow_list: bool = True
    admin_allow_retrieve: bool = True
    admin_allow_create: bool = True
    admin_allow_update: bool = True
    admin_allow_delete: bool = True


@dataclass(frozen=True)
class DefaultFormSubmissionAPISettings:
    filterset_class: Optional[str] = None
    ordering_fields: List[str] = field(default_factory=lambda: ["submitted_at"])
    search_fields: List[str] = field(
        default_factory=lambda: ["form__name", "form__description"]
    )
    allow_list: bool = True
    allow_retrieve: bool = True
    allow_create: bool = True
    allow_update: bool = False
    allow_delete: bool = False
    admin_allow_list: bool = True
    admin_allow_retrieve: bool = True
    admin_allow_create: bool = False
    admin_allow_update: bool = False
    admin_allow_delete: bool = False


admin_settings = DefaultAdminSettings()
throttle_settings = DefaultThrottleSettings()
serializer_settings = DefaultSerializerSettings()
api_settings = DefaultAPISettings()
api_dynamic_form_settings = DefaultDynamicFormAPISettings()
api_dynamic_field_settings = DefaultDynamicFieldAPISettings()
api_field_type_settings = DefaultFieldTypeAPISettings()
api_form_submission_settings = DefaultFormSubmissionAPISettings()
