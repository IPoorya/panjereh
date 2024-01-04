from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, OtpPhoneSerializer, OtpPhoneCodeSerializer
from .models import User, otp as otpModel, ValidPhone
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework import status
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiParameter


class SignUpApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    
    def post(self, request):
        srz_data = UserSerializer(data=request.data)
        if srz_data.is_valid():
            user = User.objects.create_user(
                phone_number=srz_data.validated_data['phone_number'],
                username=srz_data.validated_data['username'],
                email=srz_data.validated_data.get('email', ''),
                password=srz_data.validated_data['password']
            )
            return Response({
                "phone_number": srz_data.data['phone_number'],
                "username": srz_data.data['username'],
                "email": srz_data.data['email'],
                "tokens":{
                    'access_token': str(AccessToken.for_user(user)),
                    'refresh_token': str(RefreshToken.for_user(user)),
                    }
                }, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
            
    

class OtpPhoneApiView(APIView):
    """
    phone_number -- The phone number of the user
    """

    permission_classes = [AllowAny]
    serializer_class = OtpPhoneSerializer


    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='phone_number',
                description='The phone number of the user',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY
            ),
        ]
    )
    def get(self, request):
        srz_data = OtpPhoneSerializer(data=request.query_params)
        if srz_data.is_valid():
            otpModel.objects.create(phone_number=srz_data.validated_data['phone_number'])
            return Response({'phone_number': srz_data.data['phone_number'],
                             "message": "code sent"}, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class OtpPhoneCodeApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = OtpPhoneCodeSerializer

    def post(self, request):
        srz_data = OtpPhoneCodeSerializer(data=request.data)
        if srz_data.is_valid():
            otps = otpModel.objects.filter(phone_number=srz_data.validated_data['phone_number']).values_list('code', flat=True)
            if srz_data.validated_data['code'] in otps:
                ValidPhone.objects.create(phone_number=srz_data.validated_data['phone_number'])
                otpModel.objects.filter(phone_number=srz_data.validated_data['phone_number']).delete()
                return Response({"message":"valid!", "status":status.HTTP_202_ACCEPTED})
        return Response({'message': 'wrong code or invalid phone number!', 'status': status.HTTP_400_BAD_REQUEST})


        
