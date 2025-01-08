from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from auth_system.forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
      
    else:
        form = CustomUserCreationForm()
        messages.error(request, "some error")
    return render(request=request, 
                  template_name="auth_system/register.html",
                  context = {"form":form})

def auth_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Неправильний логін або пароль")
    else:
        form = AuthenticationForm(request=request, data=request.POST)
        messages.error(request, "some error")
    return render(request=request, 
                  template_name="auth_system/auth_login.html",
                  context = {"form":form})


def auth_logout(request):
    print(1)
    logout(request)
    context={
        "render_string":"You logged out"
    }
    return render(request=request, template_name="booking/index.html", context=context)