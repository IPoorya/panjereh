from rest_framework import serializers
from .models import ApartmentSell, ApartmentRent


class ApartmentSellSerializer(serializers.ModelSerializer):
    timestamp = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    token = serializers.ReadOnlyField()

    class Meta:
        model = ApartmentSell
        exclude = ('owner', 'id', 'visible')


class ApartmentRentSerializer(serializers.ModelSerializer):
    timestamp = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    token = serializers.ReadOnlyField()

    class Meta:
        model = ApartmentRent
        exclude = ('owner', 'id', 'visible')


class PostFiltersSerializer(serializers.Serializer):
    province = serializers.ListField(required=False, write_only=True)
    city = serializers.ListField(required=False, write_only=True)
    meterage = serializers.IntegerField(required=False, write_only=True)
    build = serializers.IntegerField(required=False, write_only=True)
    elevator = serializers.BooleanField(required=False, write_only=True)
    parking = serializers.BooleanField(required=False, write_only=True)
    storage = serializers.BooleanField(required=False, write_only=True)
    timestamp = serializers.CharField(required=False, max_length=30)
    posts = serializers.ListField(read_only=True)



