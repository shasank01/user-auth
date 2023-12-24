from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path("", views.homepage, name="index"),
    path("register", views.register, name="register"),
    path("login", LoginView.as_view(template_name="polls/login.html"), name="login"),
    path("profile", views.profile, name="profile"),
    path("logout", LogoutView.as_view(), name="logout"),
]
