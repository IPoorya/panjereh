from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignUpApiView, OtpApiView, OtpValidateApiView

app_name = "accounts"
urlpatterns = [
    path('register/send-code', OtpApiView.as_view(), name='otpApi'),
    path('register/validate-code', OtpValidateApiView.as_view(), name='otpApi'),
    path('register/signup/', SignUpApiView.as_view(), name='signup'),
    path('register/jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]