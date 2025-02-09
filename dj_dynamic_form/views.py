from rest_framework import viewsets
from .models import DynamicForm, DynamicField, FormSubmission
from .serializers import DynamicFormSerializer, DynamicFieldSerializer, FormSubmissionSerializer

class DynamicFormViewSet(viewsets.ModelViewSet):
    """
    API for managing Dynamic Forms.
    """
    queryset = DynamicForm.objects.all()
    serializer_class = DynamicFormSerializer

class DynamicFieldViewSet(viewsets.ModelViewSet):
    """
    API for managing Dynamic Fields inside a form.
    """
    queryset = DynamicField.objects.all()
    serializer_class = DynamicFieldSerializer

class FormSubmissionViewSet(viewsets.ModelViewSet):
    """
    API for managing form submissions.
    """
    queryset = FormSubmission.objects.all()
    serializer_class = FormSubmissionSerializer
