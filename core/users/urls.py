from django.urls import path
from .views import UserCreateView, UserLoginView, UserDetailView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('me/', UserDetailView.as_view(), name='user-detail'),  # Get current user info
]
