from rest_framework import serializers

class PredictRentSerializer(serializers.Serializer):
    neighbourhood = serializers.CharField(required=True, write_only=True)
    meterage = serializers.IntegerField(required=True, write_only=True)
    build = serializers.IntegerField(required=True, write_only=True)
    room = serializers.IntegerField(required=True, write_only=True)
    elevator = serializers.BooleanField(required=True, write_only=True)
    parking = serializers.BooleanField(required=True, write_only=True)
    storage = serializers.BooleanField(required=True, write_only=True)
    predictions_rent = serializers.IntegerField(read_only=True)
    predictions_deposit = serializers.IntegerField(read_only=True)
    



