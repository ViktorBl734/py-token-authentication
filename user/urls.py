from django.contrib.auth.views import LoginView
from django.urls import path

from user.views import CreateUserView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="user_register"),
    path("login/", LoginView.as_view(), name="user_token"),
    path("me/", ManageUserView.as_view(), name="manage"),

]
app_name = "user"
