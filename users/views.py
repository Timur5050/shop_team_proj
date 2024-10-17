from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def perform_create(self, serializer):
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        response = Response(serializer.data, status=status.HTTP_201_CREATED)

        response.set_cookie("access_token", str(access_token), httponly=True, secure=True)
        response.set_cookie("refresh_token", str(refresh), httponly=True, secure=True)

        return response


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        tokens = response.data

        response.set_cookie('access_token', tokens['access'], httponly=True, secure=True)
        response.set_cookie('refresh_token', tokens['refresh'], httponly=True, secure=True)
        return response
