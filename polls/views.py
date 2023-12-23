from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import UserForms, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def homepage(request):
    return render(request, "polls/index.html")


def register(request):
    form = UserForms()
    if request.method == "POST":
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {"registerform": form}
    return render(request, "polls/register.html", context=context)


# def login(request):
#     return render(request, "polls/login.html")
def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get["username"]
            password = request.POST.get["password"]
            user = authenticate(request, username=username, password=password)
            # print(user)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            # else:
            #     print("Autientication Failed")

    context = {"loginform": form}
    return render(request, "polls/login.html", context=context)


# def login_view(request):
#     print("Login view reached")  # Temporary debugging message
#     # Your existing login logic here...


@login_required(login_url="login")
def dashboard(request):
    return render(request, "polls/dashboard.html")


def my_logout(request):
    auth.logout(request)
    return redirect("login")
