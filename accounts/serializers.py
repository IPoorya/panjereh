from rest_framework import serializers
from .models import User, ValidPhone


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['id', 'is_active', 'is_admin', 'last_login', 'date_joined']

        extra_kwargs = {
            "password":{"write_only": True},
        }

    def validate_phone_number(self, value):
        if not ValidPhone.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("phone number is not validated")
        return value

    
class OtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    code = serializers.ReadOnlyField()

    def validate_phone_number(self, value):
        if ValidPhone.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("phone number already validated")
        return value


