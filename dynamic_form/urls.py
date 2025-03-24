from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DynamicFormViewSet, DynamicFieldViewSet, FormSubmissionViewSet

# Registering routes using DRF's DefaultRouter
router = DefaultRouter()
router.register(r"forms", DynamicFormViewSet)
router.register(r"fields", DynamicFieldViewSet)
router.register(r"submissions", FormSubmissionViewSet)

urlpatterns = router.urls
