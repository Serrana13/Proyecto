from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CambiarPasswordForm
from .forms import LoginForm
from .views import signup, profile, edit_profile


urlpatterns = [

    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html", authentication_form=LoginForm), name="login"),

    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),

    path("signup/", signup, name="signup"),

    path("profile/", profile, name="profile"),

    path("edit_profile/", edit_profile, name="edit_profile"),

    path(
        "password_change/", auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html", form_class=CambiarPasswordForm),
    name="password_change"
),
    path(
        "password_change_done/",
        auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"),
        name="password_change_done"
    ),

]