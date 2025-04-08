from django.shortcuts import render, redirect
from userauth.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import get_user_model

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "Account created successfully!")
            new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("home:index")  # Redirect to home after registration
    else:
        form = UserRegisterForm()
    return render(request, "userauth/sign-up.html", {"form": form})
# userauth/views.py
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            if user.role == 'owner':
                return redirect("owner:dashboard")  # Use the 'owner' namespace here
            return redirect("home:index")
        else:
            messages.warning(request, "Invalid email or password.")
    return render(request, "userauth/sign-in.html")


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("userauth:sign-in")

def aboutus(request):
    return render(request,"userauth/aboutus.html")