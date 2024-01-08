from django.urls import path
from .views import UserRegisterView, UserDetailsView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("user/", UserDetailsView.as_view(), name="user-details"),
    path("api/token/", ObtainAuthToken.as_view(), name="api-token"),
]
