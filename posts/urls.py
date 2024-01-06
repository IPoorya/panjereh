from django.urls import path
from .views import CreatePostApiView, GetPostApiView, EditPostApiView, DeletePostApiView, GetCitiesApiView, RentListApiView, SellListApiView


app_name = "posts"
urlpatterns = [
    path('post/<str:type>/create/', CreatePostApiView.as_view(), name='create_post'),
    path('post/<str:token>/', GetPostApiView.as_view(), name='get_post'),
    path('post/<str:token>/edit/', EditPostApiView.as_view(), name='edit_post'),
    path('post/<str:token>/delete/', DeletePostApiView.as_view(), name='delete_post'),
    path('cities/', GetCitiesApiView.as_view(), name='delete_post'),
    path('posts/sell/', SellListApiView.as_view(), name='sells_list'),
    path('posts/rent/', RentListApiView.as_view(), name='rents_list'),
    ]