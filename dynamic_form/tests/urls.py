from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('dynamic_form/', include("dynamic_form.api.routers.main")),
]
