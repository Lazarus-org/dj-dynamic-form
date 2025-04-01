# Welcome to the Django Dynamic Form Documentation!

[![License](https://img.shields.io/github/license/lazarus-org/dj-dynamic-form)](https://github.com/lazarus-org/dj-dynamic-form/blob/main/LICENSE)
[![PyPI Release](https://img.shields.io/pypi/v/dj-dynamic-form)](https://pypi.org/project/dj-dynamic-form/)
[![Pylint Score](https://img.shields.io/badge/pylint-10/10-brightgreen?logo=python&logoColor=blue)](https://www.pylint.org/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/dj-dynamic-form)](https://pypi.org/project/dj-dynamic-form/)
[![Supported Django Versions](https://img.shields.io/pypi/djversions/dj-dynamic-form)](https://pypi.org/project/dj-dynamic-form/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=yellow)](https://github.com/pre-commit/pre-commit)
[![Open Issues](https://img.shields.io/github/issues/lazarus-org/dj-dynamic-form)](https://github.com/lazarus-org/dj-dynamic-form/issues)
[![Last Commit](https://img.shields.io/github/last-commit/lazarus-org/dj-dynamic-form)](https://github.com/lazarus-org/dj-dynamic-form/commits/main)
[![Languages](https://img.shields.io/github/languages/top/lazarus-org/dj-dynamic-form)](https://github.com/lazarus-org/dj-dynamic-form)
[![Coverage](https://codecov.io/gh/lazarus-org/dj-dynamic-form/branch/main/graph/badge.svg)](https://codecov.io/gh/lazarus-org/dj-dynamic-form)

[`dj-dynamic-form`](https://github.com/lazarus-org/dj-dynamic-form/) is a Django package developed by Lazarus that empowers developers to create, manage, and process dynamic forms within Django applications.

It provides a robust framework for defining flexible form structures, fields, and submissions, with built-in support for Django Admin and RESTful API integration via Django REST Framework.

## Project Detail

- Language: Python >= 3.9
- Framework: Django >= 4.2
- Django REST Framework: >= 3.14

## Documentation Overview

The documentation is organized into the following sections:

- **[Quick Start](#quick-start)**: Get up and running quickly with basic setup instructions.
- **[API Guide](#api-guide)**: Detailed information on available APIs and endpoints.
- **[Admin Panel](#admin-panel)**: Detailed information on available features and functionalities of Admin Panel.
- **[Settings](#settings)**: Configuration options and settings you can customize.

---

# Quick Start

This section provides a fast and easy guide to getting the `dj-dynamic-form` package up and running in your Django
project.
Follow the steps below to quickly set up the package and start using the package.

## 1. Install the Package

**Option 1: Using `pip` (Recommended)**

Install the package via pip:

```bash
$ pip install dj-dynamic-form
```

**Option 2: Using `Poetry`**

If you're using Poetry, add the package with:

```bash
$ poetry add dj-dynamic-form
```

**Option 3: Using `pipenv`**

If you're using pipenv, install the package with:

```bash
$ pipenv install dj-dynamic-form
```

## 2. Install Django REST Framework

You need to install Django REST Framework for API support. If it's not already installed in your project, you can
install it via pip:

**Using pip:**

```bash
$ pip install djangorestframework
```

## 3. Add to Installed Apps

After installing the necessary packages, ensure that both `rest_framework` and `dynamic_form` are added to
the `INSTALLED_APPS` in your Django `settings.py` file:

```python
INSTALLED_APPS = [
    # ...
    "rest_framework",

    "dynamic_form",
    # ...
]
```

### 4. (Optional) Configure API Filters

To enable filtering through the API, install ``django-filter``, include ``django_filters`` in your ``INSTALLED_APPS``.

Install ``django-filter`` using one of the above methods:

**Using pip:**

```bash
$ pip install django-filter
```

Add `django_filters` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
   # ...
   "django_filters",
   # ...
]
```

You can also define your custom `FilterClass` and reference it in settings if needed. This allows you to customize the filtering behavior according to your requirements. for more detailed info, refer to the [Settings](#settings) section.



## 5. Apply Migrations

Run the following command to apply the necessary migrations:

```shell
python manage.py migrate
```

## 6. Add project URL routes

You can use the API or the Django Template View for Dashboard by Including them in your project’s `urls.py` file:

```python
from django.urls import path, include

urlpatterns = [
    # ...
    path("dynamic_form/", include("dynamic_form.api.routers.main")),
    # ...
]
```

----

# API Guide

This section provides a detailed overview of the `dj-dynamic-form` API, enabling administrators and users to manage dynamic forms, fields , field types, and submissions within Django and Django REST Framework (DRF) applications. The API exposes several primary endpoints grouped by functionality:

- **`/admin/forms/`**, **`/admin/forms/{form_id}/fields/`**, **`/admin/field-types/`**, **`/admin/submissions/`** - Admin APIs for managing all forms, related fields, field types and submissions (requires admin permissions).
- **`/forms/`**, **`/fields/`**, **`/field-types/`**, **`/submissions/`** - User APIs for interacting with forms, fields and submitting data.
---

## Admin API Management

The admin endpoints allow admin users (default permission is set to `IsAdminUser`) to fully manage dynamic forms, fields, and submissions. Each endpoint supports standard CRUD operations with configurable permissions.

### Dynamic Forms (`/admin/forms/`)

- **List Forms**:

  Fetches all dynamic forms. Controlled by `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_LIST`.
- **Retrieve a Form**:

  Retrieves a specific form by ID. Controlled by `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_RETRIEVE`.
- **Create a Form**:

  Creates a new form. Controlled by `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_CREATE`.
- **Update a Form**:

  Updates an existing form (e.g., toggling `is_active`). Controlled by `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_UPDATE`.
- **Delete a Form**:

  Deletes an existing form. Controlled by `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_DELETE`.

### Dynamic Fields (`/admin/forms/{form_id}/fields/`)

- **List Fields**:

  Fetches all fields for a specific form. Controlled by `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_LIST`.
- **Retrieve a Field**:

  Retrieves a specific field by ID within a form. Controlled by `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_RETRIEVE`.
- **Create a Field**:

  Creates a new field for the specified form. Controlled by `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_CREATE`.
- **Update a Field**:

  Updates an existing field (e.g., changing `is_required`). Controlled by `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_UPDATE`.
- **Delete a Field**:

  Deletes an existing field from the form. Controlled by `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_DELETE`.

### Field Types (`/admin/field-types/`)

- **List Field Types**:

  Fetches all field types. Controlled by `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_LIST`.
- **Retrieve a Field Type**:

  Retrieves a specific field type by ID. Controlled by `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_RETRIEVE`.
- **Create a Field Type**:

  Creates a new field type. Controlled by `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_CREATE`.
- **Update a Field Type**:

  Updates an existing field type (e.g., changing `is_active`). Controlled by `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_UPDATE`.
- **Delete a Field Type**:

  Deletes an existing field type. Controlled by `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_DELETE`.


### Form Submissions (`/admin/form-submissions/`)

- **List Submissions**:

  Fetches all submissions. Controlled by `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_LIST`.
- **Retrieve a Submission**:

  Retrieves a specific submission by ID. Controlled by `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_RETRIEVE`.
- **Create a Submission**:

  Creates a new submission (admin use case). Controlled by `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_CREATE`.
- **Update a Submission**:

  Updates an existing submission. Controlled by `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_UPDATE`.
- **Delete a Submission**:

  Deletes an existing submission. Controlled by `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_DELETE`.

---

## User API Management

The user endpoints allow authenticated users to interact with forms and manage their own submissions.

### Forms (`/forms/`)

- **List Forms**:

  Fetches all active forms available to users. Controlled by `DYNAMIC_FORM_API_DYNAMIC_FORM_ALLOW_LIST`.
- **Retrieve a Form**:

  Retrieves a specific form by ID. Controlled by `DYNAMIC_FORM_API_DYNAMIC_FORM_ALLOW_RETRIEVE`.

### Fields (`/fields/`)

- **List Fields**:

  Fetches all fields available to users. Controlled by `DYNAMIC_FORM_API_DYNAMIC_FIELD_ALLOW_LIST`.
- **Retrieve a Field**:

  Retrieves a specific field by ID. Controlled by `DYNAMIC_FORM_API_DYNAMIC_FIELD_ALLOW_RETRIEVE`.

### Field Types (`/field-types/`)

- **List Field Types**:

  Fetches all field types available to users. Controlled by `DYNAMIC_FORM_API_FIELD_TYPE_ALLOW_LIST`.
- **Retrieve a Field**:

  Retrieves a specific field by ID. Controlled by `DYNAMIC_FORM_API_FIELD_TYPE_ALLOW_RETRIEVE`.


### Form Submissions (`/form-submissions/`)

- **List Submissions**:

  Fetches the user's own submissions. Controlled by `DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_LIST`.
- **Retrieve a Submission**:

  Retrieves a specific user submission by ID. Controlled by `DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_RETRIEVE`.
- **Create a Submission**:

  Submits data for a form. Controlled by `DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_CREATE`.
- **Update a Submission**:

  Updates an existing user submission. Controlled by `DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_UPDATE`.
- **Delete a Submission**:

  Deletes an existing user submission. Controlled by `DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_DELETE`.

---

## Response Fields

### Forms
- `id`: Unique identifier of the form (integer).
- `name`: Name of the form (string).
- `description`: Description of the form (string).
- `is_active`: Boolean indicating if the form is active (boolean).
- `fields`: List of associated fields (nested array of field objects, included in retrieve or list responses).
- `created_at`: Timestamp when the form was created (ISO 8601 string).
- `updated_at`: Timestamp when the form was last updated (ISO 8601 string).

### Fields
- `id`: Unique identifier of the field (integer).
- `form`: ID of the associated form (integer; not included in nested responses under forms).
- `name`: Field name, unique within the form (string).
- `label`: Human-readable label for the field (string).
- `field_type`: The associated field type (nested object with `id`, `name`, `label`, `description`, `created_at`, and `is_active`).
- `is_required`: Boolean indicating if the field is mandatory (boolean).
- `choices`: List of predefined options for the field, if applicable (array or null).
- `default_value`: Default value for the field, if set (string or null).
- `validation_rules`: Custom validation rules for the field, if any (object or null).
- `order`: Order of the field within the form (integer).

### Field Types
- `id`: Unique identifier of the field type (integer).
- `name`: Name of the field type (e.g., "text", "boolean") (string).
- `label`: Human-readable label for the field type (string).
- `description`: Description of the field type (string).
- `created_at`: Timestamp when the field type was created (ISO 8601 string).
- `is_active`: Boolean indicating if the field type is active (boolean).

### Form Submissions
- `id`: Unique identifier of the submission (integer).
- `form`: The associated form (nested object with full form details, including `id`, `fields`, `name`, `description`, `is_active`, `created_at`, and `updated_at`).
- `user`: The submitting user (nested object with `username` and `email`, or null if anonymous).
- `submitted_data`: JSON object containing the submitted field values (object with field names as keys).
- `submitted_at`: Timestamp when the submission was made (ISO 8601 string).

---

### Example Responses

**List Forms**:
```text
GET /forms/ or /admin/forms

Response:
HTTP/1.1 200 OK
Content-Type: application/json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "fields": [
                {
                    "id": 1,
                    "field_type": {
                        "id": 1,
                        "name": "text",
                        "label": "Text Field",
                        "description": "A single-line text input.",
                        "created_at": "2025-03-24T17:15:23.628891Z",
                        "is_active": true
                    },
                    "name": "first_name",
                    "label": "First Name",
                    "is_required": false,
                    "choices": null,
                    "default_value": null,
                    "validation_rules": null,
                    "order": 0,
                    "form": 1
                },
                {
                    "id": 3,
                    "field_type": {
                        "id": 1,
                        "name": "text",
                        "label": "Text Field",
                        "description": "A single-line text input.",
                        "created_at": "2025-03-24T17:15:23.628891Z",
                        "is_active": true
                    },
                    "name": "last_name",
                    "label": "Last Name",
                    "is_required": false,
                    "choices": null,
                    "default_value": null,
                    "validation_rules": null,
                    "order": 0,
                    "form": 1
                },
            ],
            "name": "Test Form",
            "description": "some description",
            "is_active": true,
            "created_at": "2025-03-24T18:31:21.458061Z",
            "updated_at": "2025-03-24T18:31:21.458097Z"
        }
    ]
}
```

**Create a Form**:
```text
POST /admin/forms/
Content-Type: application/json

{
    "name": "Test Form",
    "description": "some description",
    "is_active": true
}

Response:
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 2,
    "fields": [],
    "name": "Test Form",
    "description": "some description",
    "is_active": true,
    "created_at": "2025-04-01T07:23:56.582322Z",
    "updated_at": "2025-04-01T07:23:56.582351Z"
}
```

---

**List Fields**:
```text
GET /fields/ or admin/forms/1/fields/
Response:
HTTP/1.1 200 OK
Content-Type: application/json

{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "field_type": {
                "id": 1,
                "name": "text",
                "label": "Text Field",
                "description": "A single-line text input.",
                "created_at": "2025-03-24T17:15:23.628891Z",
                "is_active": true
            },
            "name": "first_name",
            "label": "First Name",
            "is_required": false,
            "choices": null,
            "default_value": null,
            "validation_rules": null,
            "order": 0,
            "form": 1
        },
    ]
}
```

---

**Create a Field**:
```text
POST /admin/forms/1/fields/
Content-Type: application/json

{
    "field_type_id": 1,
    "name": "email",
    "label": "Email Address",
    "is_required": true
}

Response:
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 6,
    "field_type": {
        "id": 1,
        "name": "text",
        "label": "Text Field",
        "description": "A single-line text input.",
        "created_at": "2025-03-24T17:15:23.628891Z",
        "is_active": true
    },
    "name": "email",
    "label": "Email Address",
    "is_required": false,
    "choices": null,
    "default_value": null,
    "validation_rules": null,
    "order": 3,
    "form": 1
}
```

**List Field Types**:
```text
GET /field-types/ or admin/field-types/
Response:
HTTP/1.1 200 OK
Content-Type: application/json

{
    "count": 10,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4,
            "name": "boolean",
            "label": "Boolean Field",
            "description": "A true/false checkbox.",
            "created_at": "2025-03-24T17:15:23.633779Z",
            "is_active": true
        },
        {
            "id": 8,
            "name": "checkbox",
            "label": "Checkbox Field",
            "description": "A checkbox input.",
            "created_at": "2025-03-24T17:15:23.637771Z",
            "is_active": true
        },
    ]
}
```

**Create a Field Type**:
```text
POST /admin/field-types/
Content-Type: application/json

{
    "name": "boolean",
    "label": "Boolean Filed",
    "description": "A true/false checkbox.",
    "is_active": true
}

Response:
HTTP/1.1 201 Created
Content-Type: application/json
{
    "id": 4,
    "name": "boolean",
    "label": "Boolean Field",
    "description": "A true/false checkbox.",
    "created_at": "2025-03-24T17:15:23.633779Z",
    "is_active": true
}
```
---
**List Form Submissions**:
```text
GET /submissions/ or admin/submissions/
Response:
HTTP/1.1 200 OK
Content-Type: application/json

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "form": {
                "id": 1,
                "fields": [
                    {
                        "id": 1,
                        "field_type": {
                            "id": 1,
                            "name": "text",
                            "label": "Text Field",
                            "description": "A single-line text input.",
                            "created_at": "2025-03-24T17:15:23.628891Z",
                            "is_active": true
                        },
                        "name": "first_name",
                        "label": "First Name",
                        "is_required": false,
                        "choices": null,
                        "default_value": null,
                        "validation_rules": null,
                        "order": 0,
                        "form": 1
                    },
                    {
                        "id": 2,
                        "field_type": {
                            "id": 1,
                            "name": "text",
                            "label": "Text Field",
                            "description": "A single-line text input.",
                            "created_at": "2025-03-24T17:15:23.628891Z",
                            "is_active": true
                        },
                        "name": "last_name",
                        "label": "Last Name",
                        "is_required": true,
                        "choices": null,
                        "default_value": null,
                        "validation_rules": null,
                        "order": 1,
                        "form": 1
                    },
                    {
                        "id": 5,
                        "field_type": {
                            "id": 2,
                            "name": "number",
                            "label": "Number Field",
                            "description": "A numeric input.",
                            "created_at": "2025-03-24T17:15:23.631288Z",
                            "is_active": true
                        },
                        "name": "address",
                        "label": "Address",
                        "is_required": false,
                        "choices": null,
                        "default_value": null,
                        "validation_rules": null,
                        "order": 3,
                        "form": 1
                    },
                    {
                        "id": 6,
                        "field_type": {
                            "id": 1,
                            "name": "text",
                            "label": "Text Field",
                            "description": "A single-line text input.",
                            "created_at": "2025-03-24T17:15:23.628891Z",
                            "is_active": true
                        },
                        "name": "email",
                        "label": "Email Address",
                        "is_required": false,
                        "choices": null,
                        "default_value": null,
                        "validation_rules": null,
                        "order": 3,
                        "form": 1
                    }
                ],
                "name": "Login Form",
                "description": "some desc",
                "is_active": true,
                "created_at": "2025-03-24T18:31:21.458061Z",
                "updated_at": "2025-03-24T18:31:21.458097Z"
            },
            "user": {
                "username": "mehrshad",
                "email": ""
            },
            "submitted_data": {
                "last_name": "some last name"
            },
            "submitted_at": "2025-03-27T20:13:22.504769Z"
        },
    ]
}
```
---

**Create a Submission**:
```text
POST /submissions/
Content-Type: application/json

{
    "form_id": 1,
    "submitted_data": {"email": "user@example.com"}
}

Response:
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 1,
    "form": {
        "id": 1,
        "fields": [
            {
                "id": 1,
                "field_type": {
                    "id": 1,
                    "name": "text",
                    "label": "Text Field",
                    "description": "A single-line text input.",
                    "created_at": "2025-03-24T17:15:23.628891Z",
                    "is_active": true
                },
                "name": "first_name",
                "label": "First Name",
                "is_required": false,
                "choices": null,
                "default_value": null,
                "validation_rules": null,
                "order": 0,
                "form": 1
            },
            {
                "id": 2,
                "field_type": {
                    "id": 1,
                    "name": "text",
                    "label": "Text Field",
                    "description": "A single-line text input.",
                    "created_at": "2025-03-24T17:15:23.628891Z",
                    "is_active": true
                },
                "name": "last_name",
                "label": "Last Name",
                "is_required": true,
                "choices": null,
                "default_value": null,
                "validation_rules": null,
                "order": 1,
                "form": 1
            },
            {
                "id": 5,
                "field_type": {
                    "id": 2,
                    "name": "number",
                    "label": "Number Field",
                    "description": "A numeric input.",
                    "created_at": "2025-03-24T17:15:23.631288Z",
                    "is_active": true
                },
                "name": "address",
                "label": "Address",
                "is_required": false,
                "choices": null,
                "default_value": null,
                "validation_rules": null,
                "order": 3,
                "form": 1
            },
            {
                "id": 6,
                "field_type": {
                    "id": 1,
                    "name": "text",
                    "label": "Text Field",
                    "description": "A single-line text input.",
                    "created_at": "2025-03-24T17:15:23.628891Z",
                    "is_active": true
                },
                "name": "email",
                "label": "Email Address",
                "is_required": false,
                "choices": null,
                "default_value": null,
                "validation_rules": null,
                "order": 3,
                "form": 1
            }
        ],
        "name": "Login Form",
        "description": "some desc",
        "is_active": true,
        "created_at": "2025-03-24T18:31:21.458061Z",
        "updated_at": "2025-03-24T18:31:21.458097Z"
    },
    "user": null,
    "submitted_data": {"email": "user@example.com"},
    "submitted_at": "2025-03-31T12:00:00+00:00"
}
```

---

## Throttling

The API includes a built-in throttling mechanism that limits the number of requests a user can make based on their role.
You can customize these throttle limits in the settings file.

To specify the throttle rates for regular users (maybe authenticated or not) and staff members, add the following in your settings:

```ini
DYNAMIC_FORM_AUTHENTICATED_USER_THROTTLE_RATE = "100/day"
DYNAMIC_FORM_STAFF_USER_THROTTLE_RATE = "60/minute"
```

These settings define the request limits for regular and admin users.

---


## Ordering, Filtering and Search

The API supports ordering, filtering and searching for all endpoints.

Options include:

- **Ordering**: Results can be ordered by fields dedicated to each ViewSet.

- **Filtering**: By default, the filtering feature is not included. If you want to use this, you need to install `django-filter` first, then add `django_filters` to your `INSTALLED_APPS` and provide the path to your custom filter class .

- **Search**: You can search for any fields that is used is search fields.

These fields can be customized by adjusting the related configurations in your Django settings.

---

## Pagination

The API uses limit-offset pagination, allowing customization of minimum, maximum, and default page size limits.

---

## Permissions

- **User API (`/dynamic_form/`)**: Available to all anonymous users (`AllowAny`) by default, but can be customized using the related API setting.
- **Admin API (`dynamic_form/admin/`)**: Restricted to staff and superusers (`IsAdminUser`) by default, but can be customized using `DYNAMIC_FORM_API_ADMIN_PERMISSION_CLASS`.

---

## Parser Classes

The API supports multiple parser classes that control how data is processed. The default parsers include:

- ``JSONParser``
- ``MultiPartParser``
- ``FormParser``

You can modify parser classes by updating the API settings to include additional parsers or customize the existing ones
to suit your project.

---

Each feature can be configured through Django settings. For further details, refer to the [Settings](#settings) section.

----

# Admin Panel

This section provides a comprehensive guide on the functionality of the Django admin panels for managing tables.

## Admin Site

If you are using a **custom admin site** in your project, you must pass your custom admin site configuration in your
Django settings. Otherwise, Django may raise the following error during checks or the ModelAdmin will not accessible in
the Admin panel.

To resolve this, In your ``settings.py``, add the following setting to specify the path to your custom admin site class
instance.

example of a custom Admin Site:

```python
from django.contrib.admin import AdminSite


class CustomAdminSite(AdminSite):
    site_header = "Custom Admin"
    site_title = "Custom Admin Portal"
    index_title = "Welcome to the Custom Admin Portal"


# Instantiate the custom admin site as example
example_admin_site = CustomAdminSite(name="custom_admin")
```

and then reference the instance like this:

```python
DYNAMIC_FORM_ADMIN_SITE_CLASS = "path.to.example_admin_site"
```

This setup allows `dj-dynamic-form` to use your custom admin site for its Admin interface, preventing any errors and
ensuring a smooth integration with the custom admin interface.

# Dynamic Forms Admin Panel

The Django admin panel for `dj-dynamic-form` provides a robust interface for administrators to manage dynamic forms, field types, fields, and form submissions. Below are the features and configurations for each admin class, designed to streamline oversight and maintenance of these resources.

---

## DynamicFormAdmin

The `DynamicFormAdmin` class provides an admin interface for managing `DynamicForm` records.

### Features

#### List Display
The list view for dynamic form records includes:
- **ID**: The unique identifier for the form (integer).
- **Name**: The name of the form (string).
- **Is Active**: A boolean indicating whether the form is active (boolean).
- **Created At**: Timestamp when the form was created (datetime).
- **Updated At**: Timestamp when the form was last updated (datetime).

#### List Display Links
The following fields are clickable links to the detailed view:
- **ID**: Links to the detailed view of the form.
- **Name**: Links to the detailed view of the form.

#### Filtering
Admins can filter the list of forms based on:
- **Created At**: Filter by creation date.
- **Updated At**: Filter by last update date.

#### Search Functionality
Admins can search for forms using:
- **Name**: Search by the form’s name.
- **Description**: Search by the form’s description.

#### Ordering
Records are ordered by:
- **Created At**: Descending order (newest first).

#### Read-Only Fields
The following fields are marked as read-only in the detailed view:
- **Created At**: The timestamp when the form was created.
- **Updated At**: The timestamp when the form was last updated.

---

## FieldTypeAdmin

The `FieldTypeAdmin` class provides an admin interface for managing `FieldType` records.

### Features

#### List Display
The list view for field type records includes:
- **ID**: The unique identifier for the field type (integer).
- **Name**: The name of the field type (e.g., "text", "boolean") (string).
- **Label**: The human-readable label for the field type (string).
- **Is Active**: A boolean indicating whether the field type is active (boolean).
- **Created At**: Timestamp when the field type was created (datetime).

#### List Display Links
The following fields are clickable links to the detailed view:
- **ID**: Links to the detailed view of the field type.
- **Name**: Links to the detailed view of the field type.

#### Filtering
Admins can filter the list of field types based on:
- **Is Active**: Filter by active or inactive status.
- **Created At**: Filter by creation date.

#### Search Functionality
Admins can search for field types using:
- **Name**: Search by the field type’s name.
- **Description**: Search by the field type’s description.

#### Ordering
Records are ordered by:
- **Created At**: Descending order (newest first).

#### Read-Only Fields
The following field is marked as read-only in the detailed view:
- **Created At**: The timestamp when the field type was created.

---

## DynamicFieldAdmin

The `DynamicFieldAdmin` class provides an admin interface for managing `DynamicField` records within forms.

### Features

#### List Display
The list view for dynamic field records includes:
- **ID**: The unique identifier for the field (integer).
- **Name**: The name of the field (string).
- **Form**: The associated form (displayed as the form’s name).
- **Field Type**: The associated field type (displayed as the field type’s name).
- **Is Required**: A boolean indicating whether the field is mandatory (boolean).
- **Order**: The order of the field within the form (integer).

#### List Display Links
The following fields are clickable links to the detailed view:
- **ID**: Links to the detailed view of the field.
- **Name**: Links to the detailed view of the field.

#### Filtering
Admins can filter the list of fields based on:
- **Field Type**: Filter by the associated field type.
- **Is Required**: Filter by whether the field is required or not.
- **Form**: Filter by the associated form.

#### Search Functionality
Admins can search for fields using:
- **Name**: Search by the field’s name.
- **Form Name**: Search by the name of the associated form (via `form__name`).

#### Ordering
Records are ordered by:
- **Order**: Ascending order (fields sorted by their position in the form).
- **Name**: Ascending order (alphabetically within the same order).

#### Autocomplete Fields
The following fields use an autocomplete widget for easier selection:
- **Form**: Allows admins to quickly select a form from the database.
- **Field Type**: Allows admins to quickly select a field type from the database.

---

## FormSubmissionAdmin

The `FormSubmissionAdmin` class provides an admin interface for managing `FormSubmission` records.

### Features

#### List Display
The list view for form submission records includes:
- **ID**: The unique identifier for the submission (integer).
- **User**: The submitting user (displayed as the username, or empty if null).
- **Form**: The associated form (displayed as the form’s name).
- **Submitted At**: Timestamp when the submission was made (datetime).

#### List Display Links
The following fields are clickable links to the detailed view:
- **ID**: Links to the detailed view of the submission.
- **User**: Links to the detailed view of the submission.

#### Filtering
Admins can filter the list of submissions based on:
- **Submitted At**: Filter by submission date.
- **Form**: Filter by the associated form.

#### Search Functionality
Admins can search for submissions using:
- **Form Name**: Search by the name of the associated form (via `form__name`).

#### Ordering
Records are ordered by:
- **Submitted At**: Descending order (newest first).

#### Read-Only Fields
The following fields are marked as read-only in the detailed view:
- **User**: The submitting user (cannot be edited).
- **Submitted At**: The timestamp when the submission was made.
- **Submitted Data**: The JSON object containing the submitted field values.

#### Permissions
- **Add Permission**: Disabled (`has_add_permission` returns `False`), preventing admins from creating submissions manually.
- **Change Permission**: Disabled (`has_change_permission` returns `False`), preventing admins from modifying existing submissions.

#### Optimizations
- **List Select Related**: Uses `list_select_related` for `user` and `form` to optimize database queries in the list view.

----

# Settings

This section outlines the available settings for configuring the `dj-dynamic-form` package. You can customize these
settings in your Django project's `settings.py` file to tailor the behavior of the system monitor to your
needs.

## Example Settings

Below is an example configuration with default values:

```python
# Admin Settings
DYNAMIC_FORM_ADMIN_HAS_ADD_PERMISSION = True
DYNAMIC_FORM_ADMIN_HAS_CHANGE_PERMISSION = True
DYNAMIC_FORM_ADMIN_HAS_DELETE_PERMISSION = True
DYNAMIC_FORM_ADMIN_HAS_MODULE_PERMISSION = True
DYNAMIC_FORM_ADMIN_SITE_CLASS = "django.contrib.admin.sites.AdminSite"  # Default Django admin site

# Global API Settings
DYNAMIC_FORM_BASE_USER_THROTTLE_RATE = "30/minute"
DYNAMIC_FORM_STAFF_USER_THROTTLE_RATE = "100/minute"
DYNAMIC_FORM_API_ADMIN_PERMISSION_CLASS = "rest_framework.permissions.IsAdminUser"
DYNAMIC_FORM_USER_SERIALIZER_CLASS = "dynamic_form.api.serializers.user.UserSerializer"
# DYNAMIC_FORM_USER_SERIALIZER_FIELDS = [if not provided, gets USERNAME_FIELD and REQUIRED_FIELDS from user model]

# DynamicForm API Settings
DYNAMIC_FORM_API_DYNAMIC_FORM_SERIALIZER_CLASS = "dynamic_form.api.serializers.forms.DynamicFormSerializer"
DYNAMIC_FORM_API_DYNAMIC_FORM_ORDERING_FIELDS = ["created_at", "updated_at"]
DYNAMIC_FORM_API_DYNAMIC_FORM_SEARCH_FIELDS = ["name", "description"]
DYNAMIC_FORM_API_DYNAMIC_FORM_THROTTLE_CLASSES = "dynamic_form.api.throttlings.RoleBasedUserRateThrottle"
DYNAMIC_FORM_API_DYNAMIC_FORM_PAGINATION_CLASS = "dynamic_form.api.paginations.DefaultLimitOffSetPagination"
DYNAMIC_FORM_API_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS = None
DYNAMIC_FORM_API_DYNAMIC_FORM_PARSER_CLASSES = [
    "rest_framework.parsers.JSONParser",
    "rest_framework.parsers.MultiPartParser",
    "rest_framework.parsers.FormParser",
]
DYNAMIC_FORM_API_DYNAMIC_FORM_FILTERSET_CLASS = None
DYNAMIC_FORM_API_DYNAMIC_FORM_ALLOW_LIST = True
DYNAMIC_FORM_API_DYNAMIC_FORM_ALLOW_RETRIEVE = True

# Admin DynamicForm API Settings
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_SERIALIZER_CLASS = "dynamic_form.api.serializers.DynamicFormSerializer"
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ORDERING_FIELDS = ["name", "created_at", "updated_at"]
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_SEARCH_FIELDS = ["name", "description"]
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_THROTTLE_CLASSES = "dynamic_form.api.throttlings.RoleBasedUserRateThrottle"
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_PAGINATION_CLASS = "dynamic_form.api.paginations.DefaultLimitOffSetPagination"
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS = None
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_PARSER_CLASSES = [
    "rest_framework.parsers.JSONParser",
    "rest_framework.parsers.MultiPartParser",
    "rest_framework.parsers.FormParser",
]
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_FILTERSET_CLASS = None
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_LIST = True
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_RETRIEVE = True
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_CREATE = True
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_UPDATE = True
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_DELETE = True

# DynamicField API Settings
DYNAMIC_FORM_API_DYNAMIC_FIELD_SERIALIZER_CLASS = "dynamic_form.api.serializers.field.DynamicFieldSerializer"
DYNAMIC_FORM_API_DYNAMIC_FIELD_ORDERING_FIELDS = ["name", "order"]
DYNAMIC_FORM_API_DYNAMIC_FIELD_SEARCH_FIELDS = ["name", "form__name"]
DYNAMIC_FORM_API_DYNAMIC_FIELD_THROTTLE_CLASSES = "dynamic_form.api.throttlings.RoleBasedUserRateThrottle"
DYNAMIC_FORM_API_DYNAMIC_FIELD_PAGINATION_CLASS = "dynamic_form.api.paginations.DefaultLimitOffSetPagination"
DYNAMIC_FORM_API_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS = None
DYNAMIC_FORM_API_DYNAMIC_FIELD_PARSER_CLASSES = [
    "rest_framework.parsers.JSONParser",
    "rest_framework.parsers.MultiPartParser",
    "rest_framework.parsers.FormParser",
]
DYNAMIC_FORM_API_DYNAMIC_FIELD_FILTERSET_CLASS = None
DYNAMIC_FORM_API_DYNAMIC_FIELD_ALLOW_LIST = True
DYNAMIC_FORM_API_DYNAMIC_FIELD_ALLOW_RETRIEVE = True

# Admin DynamicField API Settings
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_SERIALIZER_CLASS = "dynamic_form.api.serializers.field.DynamicFieldSerializer"
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ORDERING_FIELDS = ["order"]
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_SEARCH_FIELDS = ["name", "label"]
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_THROTTLE_CLASSES = "dynamic_form.api.throttlings.RoleBasedUserRateThrottle"
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_PAGINATION_CLASS = "dynamic_form.api.paginations.DefaultLimitOffSetPagination"
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS = None
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_PARSER_CLASSES = [
    "rest_framework.parsers.JSONParser",
    "rest_framework.parsers.MultiPartParser",
    "rest_framework.parsers.FormParser",
]
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_FILTERSET_CLASS = None
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_LIST = True
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_RETRIEVE = True
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_CREATE = True
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_UPDATE = True
DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_DELETE = True

# FieldType API Settings
DYNAMIC_FORM_API_FIELD_TYPE_SERIALIZER_CLASS = "dynamic_form.api.serializers.field_type.FieldTypeSerializer"
DYNAMIC_FORM_API_FIELD_TYPE_ORDERING_FIELDS = ["created_at", "updated_at"]
DYNAMIC_FORM_API_FIELD_TYPE_SEARCH_FIELDS = ["name", "label", "description"]
DYNAMIC_FORM_API_FIELD_TYPE_THROTTLE_CLASSES = "dynamic_form.api.throttlings.RoleBasedUserRateThrottle"
DYNAMIC_FORM_API_FIELD_TYPE_PAGINATION_CLASS = "dynamic_form.api.paginations.DefaultLimitOffSetPagination"
DYNAMIC_FORM_API_FIELD_TYPE_EXTRA_PERMISSION_CLASS = None
DYNAMIC_FORM_API_FIELD_TYPE_PARSER_CLASSES = [
    "rest_framework.parsers.JSONParser",
    "rest_framework.parsers.MultiPartParser",
    "rest_framework.parsers.FormParser",
]
DYNAMIC_FORM_API_FIELD_TYPE_FILTERSET_CLASS = None
DYNAMIC_FORM_API_FIELD_TYPE_ALLOW_LIST = True
DYNAMIC_FORM_API_FIELD_TYPE_ALLOW_RETRIEVE = True

# Admin FieldType API Settings
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_SERIALIZER_CLASS = "dynamic_form.api.serializers.field_type.FieldTypeSerializer"
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ORDERING_FIELDS = ["created_at", "updated_at"]
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_SEARCH_FIELDS = ["name", "label", "description"]
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_THROTTLE_CLASSES = "dynamic_form.api.throttlings.RoleBasedUserRateThrottle"
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_PAGINATION_CLASS = "dynamic_form.api.paginations.DefaultLimitOffSetPagination"
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_EXTRA_PERMISSION_CLASS = None
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_PARSER_CLASSES = [
    "rest_framework.parsers.JSONParser",
    "rest_framework.parsers.MultiPartParser",
    "rest_framework.parsers.FormParser",
]
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_FILTERSET_CLASS = None
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_LIST = True
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_RETRIEVE = True
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_CREATE = True
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_UPDATE = True
DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_DELETE = True

# FormSubmission API Settings
DYNAMIC_FORM_API_FORM_SUBMISSION_SERIALIZER_CLASS = "dynamic_form.api.serializers.form_submission.FormSubmissionSerializer"
DYNAMIC_FORM_API_FORM_SUBMISSION_ORDERING_FIELDS = ["submitted_at"]
DYNAMIC_FORM_API_FORM_SUBMISSION_SEARCH_FIELDS = ["form__name", "form__description"]
DYNAMIC_FORM_API_FORM_SUBMISSION_THROTTLE_CLASSES = "dynamic_form.api.throttlings.RoleBasedUserRateThrottle"
DYNAMIC_FORM_API_FORM_SUBMISSION_PAGINATION_CLASS = "dynamic_form.api.paginations.DefaultLimitOffSetPagination"
DYNAMIC_FORM_API_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS = None
DYNAMIC_FORM_API_FORM_SUBMISSION_PARSER_CLASSES = [
    "rest_framework.parsers.JSONParser",
    "rest_framework.parsers.MultiPartParser",
    "rest_framework.parsers.FormParser",
]
DYNAMIC_FORM_API_FORM_SUBMISSION_FILTERSET_CLASS = None
DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_LIST = True
DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_RETRIEVE = True
DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_CREATE = True
DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_UPDATE = True
DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_DELETE = True

# Admin FormSubmission API Settings
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_SERIALIZER_CLASS = "dynamic_form.api.serializers.form_submission.FormSubmissionSerializer"
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ORDERING_FIELDS = ["submitted_at"]
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_SEARCH_FIELDS = ["form__name", "form__description"]
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_THROTTLE_CLASSES = "dynamic_form.api.throttlings.RoleBasedUserRateThrottle"
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_PAGINATION_CLASS = "dynamic_form.api.paginations.DefaultLimitOffSetPagination"
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS = None
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_PARSER_CLASSES = [
    "rest_framework.parsers.JSONParser",
    "rest_framework.parsers.MultiPartParser",
    "rest_framework.parsers.FormParser",
]
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_FILTERSET_CLASS = None
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_LIST = True
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_RETRIEVE = True
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_CREATE = False
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_UPDATE = False
DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_DELETE = False
```

# Settings Overview

Below is a detailed description of each setting in `dj-dynamic-form`, helping you understand and customize them to suit your project's requirements.

---

### `DYNAMIC_FORM_ADMIN_HAS_ADD_PERMISSION`
**Type**: `bool`
**Default**: `True`
**Description**: Controls whether administrators can add new records (e.g., forms, fields) via the admin interface. Set to `False` to disable this capability across all admin models.

---

### `DYNAMIC_FORM_ADMIN_HAS_CHANGE_PERMISSION`
**Type**: `bool`
**Default**: `True`
**Description**: Determines whether administrators can modify existing records in the admin interface. Set to `False` to make all admin models read-only for edits.

---

### `DYNAMIC_FORM_ADMIN_HAS_DELETE_PERMISSION`
**Type**: `bool`
**Default**: `True`
**Description**: Controls whether administrators can delete records via the admin interface. Set to `False` to prevent deletion of forms, fields, and submissions.

---

### `DYNAMIC_FORM_ADMIN_HAS_MODULE_PERMISSION`
**Type**: `bool`
**Default**: `True`
**Description**: Governs module-level access to the `dj-dynamic-form` admin interface. Set to `False` to restrict access to the entire admin module for all models.

---

### `DYNAMIC_FORM_ADMIN_SITE_CLASS`
**Type**: `Optional[str]`
**Default**: `"django.contrib.admin.sites.AdminSite"`
**Description**: Specifies a custom `AdminSite` class for the `dj-dynamic-form` admin interface. Use this to integrate a custom admin site subclass, enhancing the admin panel's appearance or behavior. Set to `None` to use a different default site.

---

### `DYNAMIC_FORM_BASE_USER_THROTTLE_RATE`
**Type**: `str`
**Default**: `"30/minute"`
**Description**: Sets the API throttle rate for regular authenticated users (e.g., `"30/minute"`, `"50/hour"`). Adjust this to limit how often non-staff users can make requests.

---

### `DYNAMIC_FORM_STAFF_USER_THROTTLE_RATE`
**Type**: `str`
**Default**: `"100/minute"`
**Description**: Defines the API throttle rate for staff/admin users (e.g., `"100/minute"`, `"1000/day"`). Typically higher than the base rate, this can be adjusted to give privileged users more access.

---

### `DYNAMIC_FORM_API_ADMIN_PERMISSION_CLASS`
**Type**: `Optional[str]`
**Default**: `"rest_framework.permissions.IsAdminUser"`
**Description**: Specifies the DRF permission class for admin-level API endpoints. Customize this (e.g., `"path.to.CustomPermission"`) to enforce specific access rules for admin views.

---

### `DYNAMIC_FORM_USER_SERIALIZER_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.serializers.user.UserSerializer"`
**Description**: Defines the serializer class for user objects in API responses. Customize this (e.g., `"myapp.serializers.CustomUserSerializer"`) to change how user data is serialized.

---

### `DYNAMIC_FORM_API_USER_SERIALIZER_FIELDS`
**Type**: `List[str]`
**Default**: Uses `USERNAME_FIELD` and `REQUIRED_FIELDS` from the user model if not provided
**Description**: Specifies the fields included in the user serializer output. Adjust this list to expose only the desired user attributes in API responses (e.g., `["id", "username", "email"]`).

---

### `DYNAMIC_FORM_API_DYNAMIC_FORM_SERIALIZER_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.serializers.forms.DynamicFormSerializer"`
**Description**: Defines the serializer class for `DynamicForm` objects in public API endpoints. Customize this to alter how forms are serialized for non-admin users.

---

### `DYNAMIC_FORM_API_DYNAMIC_FORM_ORDERING_FIELDS`
**Type**: `List[str]`
**Default**: `["created_at", "updated_at"]`
**Description**: Lists fields that can be used to order `DynamicForm` API responses. Add or remove fields to control sorting options for form listings.

---

### `DYNAMIC_FORM_API_DYNAMIC_FORM_SEARCH_FIELDS`
**Type**: `List[str]`
**Default**: `["name", "description"]`
**Description**: Specifies fields searchable in `DynamicForm` API endpoints. Modify this to allow filtering forms by additional attributes.

---

### `DYNAMIC_FORM_API_DYNAMIC_FORM_THROTTLE_CLASSES`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.throttlings.RoleBasedUserRateThrottle"`
**Description**: Defines the throttle class for `DynamicForm` API endpoints. Set to a custom path (e.g., `"myapp.throttles.CustomThrottle"`) or `None` to disable throttling.

---

### `DYNAMIC_FORM_API_DYNAMIC_FORM_PAGINATION_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.paginations.DefaultLimitOffSetPagination"`
**Description**: Specifies the pagination class for `DynamicForm` API responses. Customize this (e.g., `"myapp.pagination.CustomPagination"`) or set to `None` to disable pagination.

---

### `DYNAMIC_FORM_API_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Adds an extra DRF permission class for `DynamicForm` API endpoints. Use this (e.g., `"myapp.permissions.ExtraPermission"`) for additional access control.

---

### `DYNAMIC_FORM_API_DYNAMIC_FORM_PARSER_CLASSES`
**Type**: `List[str]`
**Default**: Standard DRF parsers (`JSONParser`, `MultiPartParser`, `FormParser`)
**Description**: Lists parser classes for handling `DynamicForm` API request data. Modify this to support additional content types or restrict parsing options.

---

### `DYNAMIC_FORM_API_DYNAMIC_FORM_FILTERSET_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Specifies a custom `django-filter` filterset class for `DynamicForm` API endpoints. Set to a path (e.g., `"myapp.filters.FormFilter"`) to enable advanced filtering.

---

### `DYNAMIC_FORM_API_DYNAMIC_FORM_ALLOW_LIST`
**Type**: `bool`
**Default**: `True`
**Description**: Enables listing all forms via the public `DynamicForm` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_DYNAMIC_FORM_ALLOW_RETRIEVE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows retrieving individual forms by ID via the public `DynamicForm` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_SERIALIZER_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.serializers.DynamicFormSerializer"`
**Description**: Defines the serializer class for `DynamicForm` objects in admin API endpoints. Customize this for admin-specific form serialization.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ORDERING_FIELDS`
**Type**: `List[str]`
**Default**: `["name", "created_at", "updated_at"]`
**Description**: Lists fields for ordering `DynamicForm` responses in admin API endpoints. Adjust this to customize admin sorting options.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_SEARCH_FIELDS`
**Type**: `List[str]`
**Default**: `["name", "description"]`
**Description**: Specifies searchable fields in admin `DynamicForm` API endpoints. Modify this to enhance admin search capabilities.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_THROTTLE_CLASSES`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.throttlings.RoleBasedUserRateThrottle"`
**Description**: Defines the throttle class for admin `DynamicForm` API endpoints. Customize or set to `None` as needed.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_PAGINATION_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.paginations.DefaultLimitOffSetPagination"`
**Description**: Specifies the pagination class for admin `DynamicForm` API responses. Adjust or disable as required.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_EXTRA_PERMISSION_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Adds an extra permission class for admin `DynamicForm` API endpoints. Use this for additional admin access control.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_PARSER_CLASSES`
**Type**: `List[str]`
**Default**: Standard DRF parsers (`JSONParser`, `MultiPartParser`, `FormParser`)
**Description**: Lists parser classes for admin `DynamicForm` API requests. Customize to support specific data formats.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_FILTERSET_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Specifies a custom filterset class for admin `DynamicForm` API endpoints. Enable advanced filtering with a custom path.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_LIST`
**Type**: `bool`
**Default**: `True`
**Description**: Enables listing all forms via the admin `DynamicForm` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_RETRIEVE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows retrieving individual forms by ID via the admin `DynamicForm` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_CREATE`
**Type**: `bool`
**Default**: `True`
**Description**: Permits creating new forms via the admin `DynamicForm` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_UPDATE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows updating existing forms via the admin `DynamicForm` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FORM_ALLOW_DELETE`
**Type**: `bool`
**Default**: `True`
**Description**: Permits deleting forms via the admin `DynamicForm` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_DYNAMIC_FIELD_SERIALIZER_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.serializers.field.DynamicFieldSerializer"`
**Description**: Defines the serializer class for `DynamicField` objects in public API endpoints. Customize this for field serialization.

---

### `DYNAMIC_FORM_API_DYNAMIC_FIELD_ORDERING_FIELDS`
**Type**: `List[str]`
**Default**: `["name", "order"]`
**Description**: Lists fields for ordering `DynamicField` API responses. Adjust to control field sorting options.

---

### `DYNAMIC_FORM_API_DYNAMIC_FIELD_SEARCH_FIELDS`
**Type**: `List[str]`
**Default**: `["name", "form__name"]`
**Description**: Specifies searchable fields in `DynamicField` API endpoints. Modify to enhance field search capabilities.

---

### `DYNAMIC_FORM_API_DYNAMIC_FIELD_THROTTLE_CLASSES`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.throttlings.RoleBasedUserRateThrottle"`
**Description**: Defines the throttle class for `DynamicField` API endpoints. Customize or disable as needed.

---

### `DYNAMIC_FORM_API_DYNAMIC_FIELD_PAGINATION_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.paginations.DefaultLimitOffSetPagination"`
**Description**: Specifies the pagination class for `DynamicField` API responses. Adjust or disable pagination.

---

### `DYNAMIC_FORM_API_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Adds an extra permission class for `DynamicField` API endpoints. Use this for additional access control.

---

### `DYNAMIC_FORM_API_DYNAMIC_FIELD_PARSER_CLASSES`
**Type**: `List[str]`
**Default**: Standard DRF parsers (`JSONParser`, `MultiPartParser`, `FormParser`)
**Description**: Lists parser classes for `DynamicField` API requests. Customize to support specific data formats.

---

### `DYNAMIC_FORM_API_DYNAMIC_FIELD_FILTERSET_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Specifies a custom filterset class for `DynamicField` API endpoints. Enable advanced filtering with a custom path.

---

### `DYNAMIC_FORM_API_DYNAMIC_FIELD_ALLOW_LIST`
**Type**: `bool`
**Default**: `True`
**Description**: Enables listing all fields via the public `DynamicField` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_DYNAMIC_FIELD_ALLOW_RETRIEVE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows retrieving individual fields by ID via the public `DynamicField` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_SERIALIZER_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.serializers.field.DynamicFieldSerializer"`
**Description**: Defines the serializer class for `DynamicField` objects in admin API endpoints. Customize for admin-specific field serialization.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ORDERING_FIELDS`
**Type**: `List[str]`
**Default**: `["order"]`
**Description**: Lists fields for ordering `DynamicField` responses in admin API endpoints. Adjust to customize admin sorting.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_SEARCH_FIELDS`
**Type**: `List[str]`
**Default**: `["name", "label"]`
**Description**: Specifies searchable fields in admin `DynamicField` API endpoints. Modify to enhance admin search capabilities.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_THROTTLE_CLASSES`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.throttlings.RoleBasedUserRateThrottle"`
**Description**: Defines the throttle class for admin `DynamicField` API endpoints. Customize or disable as needed.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_PAGINATION_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.paginations.DefaultLimitOffSetPagination"`
**Description**: Specifies the pagination class for admin `DynamicField` API responses. Adjust or disable pagination.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_EXTRA_PERMISSION_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Adds an extra permission class for admin `DynamicField` API endpoints. Use this for additional admin access control.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_PARSER_CLASSES`
**Type**: `List[str]`
**Default**: Standard DRF parsers (`JSONParser`, `MultiPartParser`, `FormParser`)
**Description**: Lists parser classes for admin `DynamicField` API requests. Customize to support specific data formats.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_FILTERSET_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Specifies a custom filterset class for admin `DynamicField` API endpoints. Enable advanced filtering with a custom path.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_LIST`
**Type**: `bool`
**Default**: `True`
**Description**: Enables listing all fields via the admin `DynamicField` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_RETRIEVE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows retrieving individual fields by ID via the admin `DynamicField` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_CREATE`
**Type**: `bool`
**Default**: `True`
**Description**: Permits creating new fields via the admin `DynamicField` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_UPDATE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows updating existing fields via the admin `DynamicField` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_DYNAMIC_FIELD_ALLOW_DELETE`
**Type**: `bool`
**Default**: `True`
**Description**: Permits deleting fields via the admin `DynamicField` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_FIELD_TYPE_SERIALIZER_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.serializers.field_type.FieldTypeSerializer"`
**Description**: Defines the serializer class for `FieldType` objects in public API endpoints. Customize this for field type serialization.

---

### `DYNAMIC_FORM_API_FIELD_TYPE_ORDERING_FIELDS`
**Type**: `List[str]`
**Default**: `["created_at", "updated_at"]`
**Description**: Lists fields for ordering `FieldType` API responses. Adjust to control field type sorting options.

---

### `DYNAMIC_FORM_API_FIELD_TYPE_SEARCH_FIELDS`
**Type**: `List[str]`
**Default**: `["name", "label", "description"]`
**Description**: Specifies searchable fields in `FieldType` API endpoints. Modify to enhance field type search capabilities.

---

### `DYNAMIC_FORM_API_FIELD_TYPE_THROTTLE_CLASSES`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.throttlings.RoleBasedUserRateThrottle"`
**Description**: Defines the throttle class for `FieldType` API endpoints. Customize or disable as needed.

---

### `DYNAMIC_FORM_API_FIELD_TYPE_PAGINATION_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.paginations.DefaultLimitOffSetPagination"`
**Description**: Specifies the pagination class for `FieldType` API responses. Adjust or disable pagination.

---

### `DYNAMIC_FORM_API_FIELD_TYPE_EXTRA_PERMISSION_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Adds an extra permission class for `FieldType` API endpoints. Use this for additional access control.

---

### `DYNAMIC_FORM_API_FIELD_TYPE_PARSER_CLASSES`
**Type**: `List[str]`
**Default**: Standard DRF parsers (`JSONParser`, `MultiPartParser`, `FormParser`)
**Description**: Lists parser classes for `FieldType` API requests. Customize to support specific data formats.

---

### `DYNAMIC_FORM_API_FIELD_TYPE_FILTERSET_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Specifies a custom filterset class for `FieldType` API endpoints. Enable advanced filtering with a custom path.

---

### `DYNAMIC_FORM_API_FIELD_TYPE_ALLOW_LIST`
**Type**: `bool`
**Default**: `True`
**Description**: Enables listing all field types via the public `FieldType` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_FIELD_TYPE_ALLOW_RETRIEVE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows retrieving individual field types by ID via the public `FieldType` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_SERIALIZER_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.serializers.field_type.FieldTypeSerializer"`
**Description**: Defines the serializer class for `FieldType` objects in admin API endpoints. Customize for admin-specific field type serialization.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ORDERING_FIELDS`
**Type**: `List[str]`
**Default**: `["created_at", "updated_at"]`
**Description**: Lists fields for ordering `FieldType` responses in admin API endpoints. Adjust to customize admin sorting.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_SEARCH_FIELDS`
**Type**: `List[str]`
**Default**: `["name", "label", "description"]`
**Description**: Specifies searchable fields in admin `FieldType` API endpoints. Modify to enhance admin search capabilities.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_THROTTLE_CLASSES`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.throttlings.RoleBasedUserRateThrottle"`
**Description**: Defines the throttle class for admin `FieldType` API endpoints. Customize or disable as needed.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_PAGINATION_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.paginations.DefaultLimitOffSetPagination"`
**Description**: Specifies the pagination class for admin `FieldType` API responses. Adjust or disable pagination.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_EXTRA_PERMISSION_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Adds an extra permission class for admin `FieldType` API endpoints. Use this for additional admin access control.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_PARSER_CLASSES`
**Type**: `List[str]`
**Default**: Standard DRF parsers (`JSONParser`, `MultiPartParser`, `FormParser`)
**Description**: Lists parser classes for admin `FieldType` API requests. Customize to support specific data formats.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_FILTERSET_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Specifies a custom filterset class for admin `FieldType` API endpoints. Enable advanced filtering with a custom path.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_LIST`
**Type**: `bool`
**Default**: `True`
**Description**: Enables listing all field types via the admin `FieldType` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_RETRIEVE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows retrieving individual field types by ID via the admin `FieldType` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_CREATE`
**Type**: `bool`
**Default**: `True`
**Description**: Permits creating new field types via the admin `FieldType` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_UPDATE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows updating existing field types via the admin `FieldType` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_FIELD_TYPE_ALLOW_DELETE`
**Type**: `bool`
**Default**: `True`
**Description**: Permits deleting field types via the admin `FieldType` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_SERIALIZER_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.serializers.form_submission.FormSubmissionSerializer"`
**Description**: Defines the serializer class for `FormSubmission` objects in public API endpoints. Customize this for submission serialization.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_ORDERING_FIELDS`
**Type**: `List[str]`
**Default**: `["submitted_at"]`
**Description**: Lists fields for ordering `FormSubmission` API responses. Adjust to control submission sorting options.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_SEARCH_FIELDS`
**Type**: `List[str]`
**Default**: `["form__name", "form__description"]`
**Description**: Specifies searchable fields in `FormSubmission` API endpoints. Modify to enhance submission search capabilities.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_THROTTLE_CLASSES`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.throttlings.RoleBasedUserRateThrottle"`
**Description**: Defines the throttle class for `FormSubmission` API endpoints. Customize or disable as needed.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_PAGINATION_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.paginations.DefaultLimitOffSetPagination"`
**Description**: Specifies the pagination class for `FormSubmission` API responses. Adjust or disable pagination.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Adds an extra permission class for `FormSubmission` API endpoints. Use this for additional access control.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_PARSER_CLASSES`
**Type**: `List[str]`
**Default**: Standard DRF parsers (`JSONParser`, `MultiPartParser`, `FormParser`)
**Description**: Lists parser classes for `FormSubmission` API requests. Customize to support specific data formats.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_FILTERSET_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Specifies a custom filterset class for `FormSubmission` API endpoints. Enable advanced filtering with a custom path.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_LIST`
**Type**: `bool`
**Default**: `True`
**Description**: Enables listing all submissions via the public `FormSubmission` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_RETRIEVE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows retrieving individual submissions by ID via the public `FormSubmission` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_CREATE`
**Type**: `bool`
**Default**: `True`
**Description**: Permits creating new submissions via the public `FormSubmission` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_UPDATE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows updating existing submissions via the public `FormSubmission` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_FORM_SUBMISSION_ALLOW_DELETE`
**Type**: `bool`
**Default**: `True`
**Description**: Permits deleting submissions via the public `FormSubmission` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_SERIALIZER_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.serializers.form_submission.FormSubmissionSerializer"`
**Description**: Defines the serializer class for `FormSubmission` objects in admin API endpoints. Customize for admin-specific submission serialization.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ORDERING_FIELDS`
**Type**: `List[str]`
**Default**: `["submitted_at"]`
**Description**: Lists fields for ordering `FormSubmission` responses in admin API endpoints. Adjust to customize admin sorting.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_SEARCH_FIELDS`
**Type**: `List[str]`
**Default**: `["form__name", "form__description"]`
**Description**: Specifies searchable fields in admin `FormSubmission` API endpoints. Modify to enhance admin search capabilities.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_THROTTLE_CLASSES`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.throttlings.RoleBasedUserRateThrottle"`
**Description**: Defines the throttle class for admin `FormSubmission` API endpoints. Customize or disable as needed.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_PAGINATION_CLASS`
**Type**: `Optional[str]`
**Default**: `"dynamic_form.api.paginations.DefaultLimitOffSetPagination"`
**Description**: Specifies the pagination class for admin `FormSubmission` API responses. Adjust or disable pagination.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_EXTRA_PERMISSION_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Adds an extra permission class for admin `FormSubmission` API endpoints. Use this for additional admin access control.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_PARSER_CLASSES`
**Type**: `List[str]`
**Default**: Standard DRF parsers (`JSONParser`, `MultiPartParser`, `FormParser`)
**Description**: Lists parser classes for admin `FormSubmission` API requests. Customize to support specific data formats.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_FILTERSET_CLASS`
**Type**: `Optional[str]`
**Default**: `None`
**Description**: Specifies a custom filterset class for admin `FormSubmission` API endpoints. Enable advanced filtering with a custom path.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_LIST`
**Type**: `bool`
**Default**: `True`
**Description**: Enables listing all submissions via the admin `FormSubmission` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_RETRIEVE`
**Type**: `bool`
**Default**: `True`
**Description**: Allows retrieving individual submissions by ID via the admin `FormSubmission` API. Set to `False` to disable this endpoint.

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_CREATE`
**Type**: `bool`
**Default**: `False`
**Description**: Permits creating new submissions via the admin `FormSubmission` API. Set to `True` to enable this endpoint (disabled by default for admin).

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_UPDATE`
**Type**: `bool`
**Default**: `False`
**Description**: Allows updating existing submissions via the admin `FormSubmission` API. Set to `True` to enable this endpoint (disabled by default for admin).

---

### `DYNAMIC_FORM_API_ADMIN_FORM_SUBMISSION_ALLOW_DELETE`
**Type**: `bool`
**Default**: `False`
**Description**: Permits deleting submissions via the admin `FormSubmission` API. Set to `True` to enable this endpoint (disabled by default for admin).

---

### DynamicForm ViewSet - All Available Fields

These are all fields available for ordering, filtering, and searching in the `DynamicForm` ViewSet (public API):

- **`id`**: Unique identifier of the form (orderable, filterable).
  - **Description**: An integer primary key for the form record (e.g., `1`).
- **`name`**: Name of the form (searchable, filterable).
  - **Description**: A string representing the form’s name (e.g., `"Contact Form"`).
- **`description`**: Description of the form (searchable, filterable).
  - **Description**: A string providing details about the form (e.g., `"A form for user inquiries"`).
- **`is_active`**: Status indicating if the form is active (filterable).
  - **Description**: A boolean showing whether the form is active (e.g., `true` or `false`).
- **`created_at`**: Timestamp when the form was created (orderable, filterable).
  - **Description**: A datetime marking the form’s creation (e.g., `"2025-04-01T10:00:00+00:00"`).
- **`updated_at`**: Timestamp when the form was last updated (orderable, filterable).
  - **Description**: A datetime marking the form’s last update (e.g., `"2025-04-01T12:00:00+00:00"`).

---


### DynamicField ViewSet - All Available Fields

These are all fields available for ordering, filtering, and searching in the `DynamicField` ViewSet (public API):

- **`id`**: Unique identifier of the field (orderable, filterable).
  - **Description**: An integer primary key for the field record (e.g., `1`).
- **`form`**: The associated form (searchable via `form__name`, filterable via `form__id`).
  - **Description**: A foreign key to `DynamicForm`, searchable by form name (e.g., `"Contact Form"`).
- **`name`**: Field name (orderable, searchable, filterable).
  - **Description**: A unique string within the form (e.g., `"email"`).
- **`label`**: Human-readable label for the field (filterable).
  - **Description**: A string for display purposes (e.g., `"Email Address"`).
- **`field_type`**: The associated field type (filterable via `field_type__id` or `field_type__name`).
  - **Description**: A foreign key to `FieldType`, represented by its name or ID (e.g., `"text"` or `1`).
- **`is_required`**: Indicates if the field is mandatory (filterable).
  - **Description**: A boolean showing if the field must be filled (e.g., `true` or `false`).
- **`order`**: Order of the field within the form (orderable, filterable).
  - **Description**: An integer defining the field’s position (e.g., `0`).

---

### FieldType ViewSet - All Available Fields

These are all fields available for ordering, filtering, and searching in the `FieldType` ViewSet (public API):

- **`id`**: Unique identifier of the field type (orderable, filterable).
  - **Description**: An integer primary key for the field type record (e.g., `1`).
- **`name`**: Name of the field type (searchable, filterable).
  - **Description**: A string identifying the type (e.g., `"text"`).
- **`label`**: Human-readable label for the field type (searchable, filterable).
  - **Description**: A string for display (e.g., `"Text Input"`).
- **`description`**: Description of the field type (searchable, filterable).
  - **Description**: A string explaining the type (e.g., `"A simple text input field"`).
- **`created_at`**: Timestamp when the field type was created (orderable, filterable).
  - **Description**: A datetime marking the creation (e.g., `"2025-04-01T10:00:00+00:00"`).
- **`is_active`**: Status indicating if the field type is active (filterable).
  - **Description**: A boolean showing availability (e.g., `true` or `false`).

---

### FormSubmission ViewSet - All Available Fields

These are all fields available for ordering, filtering, and searching in the `FormSubmission` ViewSet (public API):

- **`id`**: Unique identifier of the submission (orderable, filterable).
  - **Description**: An integer primary key for the submission record (e.g., `1`).
- **`form`**: The associated form (searchable via `form__name` or `form__description`, filterable via `form__id`).
  - **Description**: A foreign key to `DynamicForm`, searchable by name or description (e.g., `"Contact Form"`).
- **`user`**: The submitting user (filterable via `user__id` or `user__username`).
  - **Description**: A foreign key to the user, nullable, represented by ID or username (e.g., `"user123"` or `null`).
- **`submitted_at`**: Timestamp when the submission was made (orderable, filterable).
  - **Description**: A datetime marking the submission time (e.g., `"2025-04-01T10:00:00+00:00"`).

----

# Conclusion

We hope this documentation has provided a comprehensive guide to using and understanding the `dj-dynamic-form`.

### Final Notes:

- **Version Compatibility**: Ensure your project meets the compatibility requirements for both Django and Python
  versions.
- **API Integration**: The package is designed for flexibility, allowing you to customize many features based on your
  application's needs.
- **Contributions**: Contributions are welcome! Feel free to check out the [Contributing guide](CONTRIBUTING.md) for
  more details.

If you encounter any issues or have feedback, please reach out via
our [GitHub Issues page](https://github.com/lazarus-org/dj-dynamic-form/issues).
