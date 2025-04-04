from django.urls import path, include
from .views import *


app_name = "accounts"

urlpatterns = [
    path("login-signup/", LoginView.as_view(), name="login-signup"),
    path("logout/",logout_user, name="logout"),
    path("edit-profile/", EditProfileView.as_view(), name = "edit-profile"),
    # path("change-password/", change_password, name = "change-password"),
    # path("change-password/", ChangePasswordView.as_view(), name = "change-password"),
    # path("api/v1/",include("accounts.api.v1.urls")),
]