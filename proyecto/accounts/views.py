from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegistroForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

def signup(request):

    if request.method == "POST":
        form = RegistroForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Crear perfil SOLO si no existe
            Profile.objects.get_or_create(user=user)

            return redirect("/accounts/login/")

    else:
        form = RegistroForm()

    return render(request, "accounts/signup.html", {"form": form})


@login_required
def profile(request):

    return render(request, "accounts/profile.html")


@login_required
def edit_profile(request):

    profile = request.user.profile

    if request.method == "POST":

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            return redirect("profile")

    else:

        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, "accounts/edit_profile.html", context)