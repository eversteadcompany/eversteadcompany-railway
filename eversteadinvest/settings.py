# from pathlib import Path
# import os
# from dotenv import load_dotenv
# import dj_database_url

# # Load environment variables from .env
# load_dotenv()

# # -----------------------------
# # BASE DIRECTORY
# # -----------------------------
# BASE_DIR = Path(__file__).resolve().parent.parent

# # -----------------------------
# # SECRET KEY
# # -----------------------------
# SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")  # fallback for development

# # -----------------------------
# # DEBUG
# # -----------------------------
# DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

# # -----------------------------
# # ALLOWED HOSTS
# # -----------------------------
# ALLOWED_HOSTS = [
#     ".railway.app",                 # all Railway domains
#     "eversteadinvest.com",
#     "www.eversteadinvest.com",
#     "127.0.0.1",
#     "localhost",
# ]

# # -----------------------------
# # CSRF Trusted Origins
# # -----------------------------
# CSRF_TRUSTED_ORIGINS = [
#     "https://eversteadinvest-production.up.railway.app",
#     "https://eversteadinvest.com",
#     "https://www.eversteadinvest.com",
# ]

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# # -----------------------------
# # INSTALLED APPS
# # -----------------------------
# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",

#     # Your apps
#     "home",
#     "userprofile",
#     "django_countries",
#     "investment",
#     "connectwallet",
#     "widget_tweaks",
# ]

# # -----------------------------
# # MIDDLEWARE
# # -----------------------------
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "whitenoise.middleware.WhiteNoiseMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# # -----------------------------
# # URL CONFIGURATION
# # -----------------------------
# ROOT_URLCONF = "eversteadinvest.urls"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [BASE_DIR / "templates"],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = "eversteadinvest.wsgi.application"

# # -----------------------------
# # DATABASE
# # -----------------------------
# DATABASES = {
#     "default": dj_database_url.config(
#         default=os.getenv("DATABASE_URL"),  # Railway PostgreSQL URL
#         conn_max_age=600,
#     )
# }

# # -----------------------------
# # PASSWORD VALIDATORS
# # -----------------------------
# AUTH_PASSWORD_VALIDATORS = [
#     {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
#     {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
#     {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
#     {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
# ]

# # -----------------------------
# # INTERNATIONALIZATION
# # -----------------------------
# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
# USE_I18N = True
# USE_TZ = True

# # -----------------------------
# # STATIC FILES (WhiteNoise)
# # -----------------------------
# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# # Development: additional static dirs
# if DEBUG:
#     STATICFILES_DIRS = [BASE_DIR / "static"]

# # -----------------------------
# # MEDIA FILES
# # -----------------------------
# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"

# # -----------------------------
# # LOGIN
# # -----------------------------
# LOGIN_URL = "/userprofile/login/"

# # -----------------------------
# # SECURITY
# # -----------------------------
# if not DEBUG:
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True
# else:
#     SECURE_SSL_REDIRECT = False
#     SESSION_COOKIE_SECURE = False
#     CSRF_COOKIE_SECURE = False

# # -----------------------------
# # RESEND EMAIL CONFIGURATION
# # -----------------------------
# RESEND_API_KEY = os.getenv("RESEND_API_KEY")
# if not RESEND_API_KEY and not DEBUG:
#     raise ValueError("RESEND_API_KEY environment variable is not set!")

# DEFAULT_FROM_EMAIL = "support@eversteadinvest.com"
# ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "support@eversteadinvest.com")

# # -----------------------------
# # LOGGING
# # -----------------------------
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {"class": "logging.StreamHandler"},
#     },
#     "root": {"handlers": ["console"], "level": "INFO"},
# }


from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# Load environment variables
load_dotenv()

# -----------------------------
# BASE DIRECTORY
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# SECRET KEY
# -----------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

# -----------------------------
# DEBUG
# -----------------------------
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

# -----------------------------
# ALLOWED HOSTS
# -----------------------------
ALLOWED_HOSTS = [
    ".railway.app",
    "eversteadinvest.com",
    "www.eversteadinvest.com",
    "127.0.0.1",
    "localhost",
]

# -----------------------------
# CSRF Trusted Origins
# -----------------------------
CSRF_TRUSTED_ORIGINS = [
    "https://eversteadinvest-production.up.railway.app",
    "https://eversteadinvest.com",
    "https://www.eversteadinvest.com",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# -----------------------------
# INSTALLED APPS
# -----------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Your apps
    "home",
    "userprofile",
    "django_countries",
    "investment",
    "connectwallet",
    "widget_tweaks",
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise must be directly after SecurityMiddleware
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -----------------------------
# URL CONFIGURATION
# -----------------------------
ROOT_URLCONF = "eversteadinvest.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "eversteadinvest.wsgi.application"

# -----------------------------
# DATABASE
# -----------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
    )
}

# -----------------------------
# PASSWORD VALIDATORS
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------------
# INTERNATIONALIZATION
# -----------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -----------------------------
# STATIC FILES (WhiteNoise)
# -----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# FIX: Prevent WhiteNoise from deleting un-hashed files
WHITENOISE_KEEP_ONLY_HASHED_FILES = False

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / "static"]

# -----------------------------
# MEDIA FILES
# -----------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -----------------------------
# LOGIN
# -----------------------------
LOGIN_URL = "/userprofile/login/"

# -----------------------------
# SECURITY
# -----------------------------
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
else:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

# -----------------------------
# RESEND EMAIL CONFIGURATION
# -----------------------------
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
if not RESEND_API_KEY and not DEBUG:
    raise ValueError("RESEND_API_KEY not set!")

DEFAULT_FROM_EMAIL = "support@eversteadinvest.com"
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "support@eversteadinvest.com")

# -----------------------------
# LOGGING
# -----------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}
