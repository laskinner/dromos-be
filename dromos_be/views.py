from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


@api_view()
def root_route(request):
    return Response({"message": "Welcome to my drf API!"})


@api_view(["POST"])
def logout_route(request):
    response = Response()
    response.set_cookie(
        # Access setting via django.conf.settings
        key=settings.JWT_AUTH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=settings.JWT_AUTH_SAMESITE,
        secure=settings.JWT_AUTH_SECURE,
    )
    response.set_cookie(
        # Access setting via django.conf.settings
        key=settings.JWT_AUTH_REFRESH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=settings.JWT_AUTH_SAMESITE,
        secure=settings.JWT_AUTH_SECURE,
    )
    return response


@ensure_csrf_cookie
def set_csrf_token(request):
    return JsonResponse({"detail": "CSRF cookie set"})
