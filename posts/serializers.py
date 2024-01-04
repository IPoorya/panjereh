from rest_framework import serializers
from .models import ApartmentSell, ApartmentRent


class ApartmentSellSerializer(serializers.ModelSerializer):
    timestamp = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = ApartmentSell
        exclude = ('owner', 'id', 'visible')


class ApartmentRentSerializer(serializers.ModelSerializer):
    timestamp = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = ApartmentRent
        exclude = ('owner', 'id', 'visible')


