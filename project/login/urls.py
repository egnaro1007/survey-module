from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('api/login', views.LoginClass.as_view(), name='login'),
    path('api/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', views.UserRegistration.as_view(), name='user-registration'),
]
