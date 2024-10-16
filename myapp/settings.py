"""
Django settings for myapp project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from decouple import config as env_config

try:
    from decouple import config
except:
    import os
    config = os.environ.get

# Import the Cloudflare R2 config
import helpers.cloudflare.settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(=8_6$h4-r$%80hbsw*q!wz!7u*5+@1gfgfy(4%lh5@^-v))$%"

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = config("DJANGO_DEBUG", cast=bool, default=False)


ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]

CSRF_TRUSTED_ORIGINS = ['https://src-broken-dew-5673.fly.dev']  # <-- Updated!



# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myapp.urls"

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

WSGI_APPLICATION = "myapp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "es-mx"

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
#CLOUDFLARE_R2_CONFIG_OPTIONS = {}
#
#bucket_name = config("CLOUDFLARE_R2_BUCKET")
#endpoint_url = config("CLOUDFLARE_R2_BUCKET_ENDPOINT")
#access_key = config("CLOUDFLARE_R2_ACCESS_KEY")
#secret_key = config("CLOUDFLARE_R2_SECRET_KEY")
#
#if all([bucket_name, endpoint_url, access_key, secret_key]):
#    CLOUDFLARE_R2_CONFIG_OPTIONS = {
#        "bucket_name": config("CLOUDFLARE_R2_BUCKET"),
#        "default_acl": "public-read",  # "private"
#        "signature_version": "s3v4",
#        "endpoint_url": config("CLOUDFLARE_R2_BUCKET_ENDPOINT"),
#        "access_key": config("CLOUDFLARE_R2_ACCESS_KEY"),
#        "secret_key": config("CLOUDFLARE_R2_SECRET_KEY"),
#    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STORAGES = {
    "default": {
        "BACKEND": "helpers.cloudflare.storages.MediaFileStorage",
        "OPTIONS": helpers.cloudflare.settings.CLOUDFLARE_R2_CONFIG_OPTIONS,
    },
    "staticfiles": {
        "BACKEND": "helpers.cloudflare.storages.StaticFileStorage",
        "OPTIONS": helpers.cloudflare.settings.CLOUDFLARE_R2_CONFIG_OPTIONS,
    },
}

