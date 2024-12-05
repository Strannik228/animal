from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('main:animal_list')),  # Перенаправление пустого пути на animal_list
    path('', include('main.urls')),
    path('users/', include('users.urls')),
]