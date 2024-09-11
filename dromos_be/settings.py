"""
Django settings for dromos_be project.

Generated by 'django-admin startproject' using Django 3.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from datetime import timedelta

if os.path.exists("env.py"):
    import env

CLOUDINARY_STORAGE = {"CLOUDINARY_URL": os.environ.get("CLOUDINARY_URL")}
MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEV") == "1"

ALLOWED_HOSTS = ["localhost", os.environ.get("ALLOWED_HOST"), "127.0.0.1"]

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")
# Ensure the URLs include the full scheme (https://)
CSRF_TRUSTED_ORIGINS = [
    origin if origin.startswith("http") else f"https://{origin}" for origin in CSRF_TRUSTED_ORIGINS
]

CORS_ALLOWED_ORIGINS = [
    "https://dromos-0a9ced476e6f.herokuapp.com",
    "http://localhost:5173",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "cloudinary_storage",
    "django.contrib.staticfiles",
    "cloudinary",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "profiles",
    "areas",
    "nodes",
    "edges",
    "comments",
    "subscriptions",
    "permissions.apps.PermissionsConfig",
    "corsheaders",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",  #  JWT
        "rest_framework.authentication.SessionAuthentication",  # Optional for browser-based API navigation/testing
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",  # Keeps your API secure by default
    ),
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    # Cookie settings
    "AUTH_COOKIE": "my-app-auth",  # The cookie name for the JWT access token
    "AUTH_COOKIE_DOMAIN": None,  # Use None to use the domain of the request
    "AUTH_COOKIE_SECURE": True,  # Secure flag (use True if using HTTPS, False otherwise)
    "AUTH_COOKIE_HTTP_ONLY": True,  # HTTPOnly flag to prevent JS access to the cookie
    "AUTH_COOKIE_PATH": "/",  # The path of the cookie
    "AUTH_COOKIE_SAMESITE": "None",  # SameSite attribute for the cookie
    "REFRESH_COOKIE": "my-refresh-token",  # The cookie name for the JWT refresh token
    "REFRESH_COOKIE_DOMAIN": None,  # Use None to use the domain of the request
    "REFRESH_COOKIE_SECURE": True,  # Secure flag (use True if using HTTPS, False otherwise)
    "REFRESH_COOKIE_HTTP_ONLY": True,  # HTTPOnly flag to prevent JS access to the cookie
    "REFRESH_COOKIE_PATH": "/api/token/refresh/",  # Path where the refresh token is sent
    "REFRESH_COOKIE_SAMESITE": "None",  # SameSite attribute for the cookie
}

REST_USE_JWT = True
DJANGO_REST_AUTH = {
    "USE_JWT": True,
    "SESSION_LOGIN": False,
}

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "dromos_be.serializers.CurrentUserSerializer",
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # Handle cross-origin requests
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Serve static files
    "django.middleware.security.SecurityMiddleware",  # Various security enhancements
    "django.contrib.sessions.middleware.SessionMiddleware",  # Manage user sessions
    "django.middleware.common.CommonMiddleware",  # Various tasks such as blocking User-Agents, handling redirects, etc.
    "django.middleware.csrf.CsrfViewMiddleware",  # Prevent CSRF attacks
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Bind user to request
    "django.contrib.messages.middleware.MessageMiddleware",  # Flash messages handling
    "allauth.account.middleware.AccountMiddleware",  # Integration for django-allauth
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Prevent clickjacking
]

if "CLIENT_ORIGIN" in os.environ:
    CORS_ALLOWED_ORIGINS = [os.environ.get("CLIENT_ORIGIN")]
else:
    # Allow localhost for local development
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^http://localhost:3000$",
        r"^http://127.0.0.1:3000$",
    ]

CORS_ALLOW_CREDENTIALS = True


ROOT_URLCONF = "dromos_be.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dromos_be.wsgi.application"


# Database configuration

if os.environ.get("DEV") == "1":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
    print("connected")

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


SITE_ID = 1
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# CSRF Settings
# Ensure CSRF and session cookies are set to use SameSite=None; Secure for cross-site requests
CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_NAME = (
    "csrftoken"  # Ensure the CSRF cookie name matches what is used by front-end
)
CSRF_COOKIE_HTTPONLY = (
    False  # Ensure this is False so the token is accessible via front-end
)
