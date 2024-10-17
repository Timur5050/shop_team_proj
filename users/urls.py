from django.urls import path

from users.views import CreateUserView, CustomTokenObtainPairView

urlpatterns = [
    path("registration/", CreateUserView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
]
