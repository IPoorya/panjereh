from django.urls import path
from .views import CreatePostApiView, GetPostApiView, EditPostApiView, DeletePostApiView
# , PostListApiView


app_name = "posts"
urlpatterns = [
    path('<str:type>/create/', CreatePostApiView.as_view(), name='create_post'),
    path('<int:timestamp>/', GetPostApiView.as_view(), name='get_post'),
    path('<int:timestamp>/edit/', EditPostApiView.as_view(), name='edit_post'),
    path('<int:timestamp>/delete/', DeletePostApiView.as_view(), name='delete_post'),
    # path('posts/', PostListApiView.as_view(), name='posts'),
    ]