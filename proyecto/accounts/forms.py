from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class RegistroForm(UserCreationForm):

    username = forms.CharField(
        label="Usuario",
        help_text="Obligatorio."
    )

    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    email = forms.EmailField(label="Correo electrónico")

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        help_text="""
        <ul>
            <li>La contraseña debe tener al menos 8 caracteres.</li>
            <li>No puede ser completamente numérica.</li>
        </ul>
        """
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
        help_text="Introduce la misma contraseña para verificar."
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            "bio",
        ]

class CambiarPasswordForm(PasswordChangeForm):

    old_password = forms.CharField(
        label="Contraseña actual",
        widget=forms.PasswordInput
    )

    new_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput,
        help_text="""
        <ul>
            <li>La contraseña no puede ser demasiado similar a tu información personal.</li>
            <li>Debe contener al menos 8 caracteres.</li>
            <li>No puede ser una contraseña común.</li>
            <li>No puede estar compuesta solo por números.</li>
        </ul>
        """
    )

    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput,
        help_text="Introduce la misma contraseña para verificar."
    )

class LoginForm(AuthenticationForm):

    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    error_messages = {
        "invalid_login": "Usuario o contraseña incorrectos.",
        "inactive": "Esta cuenta está inactiva.",
    }