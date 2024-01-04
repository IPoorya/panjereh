from rest_framework import serializers
from .models import User, ValidPhone


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            "password":{"write_only": True},
            # "last_login":{"write_only":True},
            # "date_joined":{"write_only":True},
            # "is_admin":{"write_only":True},
            # "is_active":{"write_only":True},
        }

    def validate_phone_number(self, value):
        if not ValidPhone.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("phone number is not validated")
        return value

class OTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    code = serializers.CharField(max_length=10, default='')

    def validate_phone_number(self, value):
        if ValidPhone.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("phone number already validated")
        return value


class PhoneIsValidSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValidPhone
        fields = 'phone_number'