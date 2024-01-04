from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignUpApiView, OTPApiView

app_name = "accounts"
urlpatterns = [
    path('', OTPApiView.as_view(), name='otpApi'),
    path('signup/', SignUpApiView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]