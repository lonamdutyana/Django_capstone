# user_auth/urls.py
from django.urls import path
from .views import register_user, login_user, logout_user

app_name = 'user_auth'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    # ... other authentication URLs as needed
]
