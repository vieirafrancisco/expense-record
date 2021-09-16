from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("expense_record.apps.api.urls")),
    path("admin/", admin.site.urls),
]
