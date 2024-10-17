from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.deprecation import MiddlewareMixin
from rest_framework.exceptions import AuthenticationFailed


class RefreshTokenMiddleware(MiddlewareMixin):
    def process_request(self, request):

        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')

        if access_token:
            try:
                JWTAuthentication().get_validated_token(access_token)
            except AuthenticationFailed:
                if refresh_token:
                    try:
                        new_token = RefreshToken(refresh_token).access_token
                        request.COOKIES['access_token'] = str(new_token)
                    except Exception:
                        pass
