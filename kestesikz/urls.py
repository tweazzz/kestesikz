from django.contrib import admin
from django.urls import path, include
from djoser.views import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]