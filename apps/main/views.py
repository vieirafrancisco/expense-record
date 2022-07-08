from datetime import date
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.main.models import Profile
from apps.main.serializers import ProfileModelSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileModelSerializer

    @action(detail=True, methods=["get"], url_path="purchase-power")
    def purchase_power(self, request, pk=None):
        today = date.today()
        month = int(request.GET.get("month", today.month))
        year = int(request.GET.get("year", today.year))
        profile = get_object_or_404(Profile, pk=pk)

        return Response(
            {"amount": profile.get_purchase_power_amount(date(year, month, 1))}
        )
