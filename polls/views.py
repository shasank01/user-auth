from functools import cache
from multiprocessing import context

# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib import messages

# Create your views here.
from .forms import UserForms, LoginForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control


def homepage(request):
    login_url = reverse("login")
    register_url = reverse("register")
    return render(
        request,
        "polls/index.html",
        {"login_url": login_url, "register_url": register_url},
    )


def register(request):
    form = UserForms()
    if request.method == "POST":
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {"registerform": form}
    return render(request, "polls/register.html", context=context)


login_view = LoginView.as_view(template_name="polls/login.html")


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                # Add a message to inform the user of authentication failure
                messages.error(
                    request, ("Invalid username or password. Please try again.")
                )
    context = {"loginform": form}
    return render(request, "polls/login.html", context=context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def profile(request):
    return render(request, "polls/profile.html")


def logout_user(request):
    auth.logout(request)
    return redirect(reverse("index"))
