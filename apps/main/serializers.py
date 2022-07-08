from rest_framework import serializers
from .models import Bill, Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class BillModelSerializer(serializers.ModelSerializer):
    profile = ProfileModelSerializer()
    class Meta:
        model = Bill
        fields = "__all__"