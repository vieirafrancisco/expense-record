from django.urls import path, include  # noqa
from rest_framework import routers  # noqa

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
]
