from django.urls import path
from .views import PricePerMeter, PredictRentPrice


app_name = "features"
urlpatterns = [
    path('features/price_per_meter/', PricePerMeter.as_view(), name='price_per_meter'),
    path('features/appartment_rent_predict/', PredictRentPrice.as_view(), name='appartment_rent_predict'),
    ]