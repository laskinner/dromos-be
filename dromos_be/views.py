from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({"message": "Welcome to my drf API!"})


@api_view(["POST"])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=settings.JWT_AUTH_COOKIE,  # Access setting via django.conf.settings
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=settings.JWT_AUTH_SAMESITE,  # Access setting via django.conf.settings
        secure=settings.JWT_AUTH_SECURE,  # Access setting via django.conf.settings
    )
    response.set_cookie(
        key=settings.JWT_AUTH_REFRESH_COOKIE,  # Access setting via django.conf.settings
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=settings.JWT_AUTH_SAMESITE,  # Access setting via django.conf.settings
        secure=settings.JWT_AUTH_SECURE,  # Access setting via django.conf.settings
    )
    return response
