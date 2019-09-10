from django.urls import path

from user import views

app_name = "user"

urlpatterns = [
    path("signup/", views.CreateUserView.as_view(), name="signup"),
    path("auth/", views.CreateTokenView.as_view(), name="auth"),
    path("me/", views.ManageUserView.as_view(), name="me"),
]
