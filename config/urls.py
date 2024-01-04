from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('accounts.urls', namespace='accounts')),
    path('post/', include('posts.urls', namespace='posts')),
]
