from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, MyUserCreationForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect("/api/events/")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect("/api/events/")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


def regitsterPage(request):
    if request.user.is_authenticated:
        return redirect("/api/events/")

    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("/api/events/")
        else:
            print(form.errors)

    else:
        form = MyUserCreationForm()

    return render(request, "accounts/signup.html", {"page": "register", "form": form})
