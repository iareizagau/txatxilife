# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config
from unipath import Path
from django.utils.translation import gettext_lazy as _
from google.oauth2 import service_account
import tempfile
import json


def key_tempfile(key_string):
    key_dict = json.loads(key_string)
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        json.dump(key_dict, temp_file)
        return temp_file.name


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)
print("DEBUG", DEBUG)

# load production server from .env
ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1',
                 config('SERVER', default='127.0.0.1')]

CSRF_TRUSTED_ORIGINS = [f"https://{config('SERVER', default='127.0.0.1')}"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'apps.home',  # Enable the inner home (home)
    'apps.maps',
    'pwa',
    'parler',
    'rosetta',
    'ninja_jwt',
    'ninja_extra',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # multi language
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'core.urls'
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'OPTIONS': {
            'client_encoding': 'UTF8',
            'options': '-c search_path=public'
        },
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

LANGUAGES = (
    ('en', _('Ingelesa')),
    ('eu', _('Euskara')),
    ('es', _('Gaztelera')),
)

PARLER_LANGUAGES = {
    None: (
        {'code': 'eu', },  # Basque
        {'code': 'en', },  # English
        {'code': 'es', },  # Spanish
    ),
    'default': {
        'fallbacks': ['eu'],
        'hide_untranslated': False,
    }
}

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale/')]

SITE_ID = 1

LOGIN_REDIRECT = 'maps:home'
LOGIN_REDIRECT_URL = 'maps:home'
LOGOUT_REDIRECT_URL = 'maps:home'  # Este no está haciendo caso, quizás haya que sobreecribir la view
LOGOUT_URL = 'account_logout'
LOGIN_URL = 'maps/home'

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = os.getenv("ACCOUNT_DEFAULT_HTTP_PROTOCOL")
ACCOUNT_LOGOUT_REDIRECT = 'maps:home'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SERVICE_ACCOUNT = os.getenv('SERVICE_ACCOUNT')
GS_BUCKET_NAME = 'txatxilife'
GS_PROJECT_ID = 'optimum-shore-409919'
GS_FILE_OVERWRITE = True
GS_MAX_MEMORY_SIZE = 0
GS_BLOB_CHUNK_SIZE = None
GS_CUSTOM_ENDPOINT_ = 'https://storage.googleapis.com'
GS_LOCATION = ''
if SERVICE_ACCOUNT and False:
    if DEBUG is False:
        SERVICE_ACCOUNT = key_tempfile(SERVICE_ACCOUNT)
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT)
    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'  # For serving static files directly from GCS
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'  # For storing media files in GCS
    STATIC_URL = f'{GS_CUSTOM_ENDPOINT_}/{GS_BUCKET_NAME}/apps/static/'
    MEDIA_URL = f'{GS_CUSTOM_ENDPOINT_}/{GS_BUCKET_NAME}/apps/media/'

STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(CORE_DIR, 'apps/static')]

MEDIA_ROOT = os.path.join(CORE_DIR, 'apps/media')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
