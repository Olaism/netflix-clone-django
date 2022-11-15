from django.urls import path

from .views import (
    UserRegistrationView,
    ProfileView,
)

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
]