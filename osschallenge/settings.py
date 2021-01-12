"""
Django settings for osschallenge project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import environ


env = environ.Env()
ROOT_DIR = environ.Path(__file__) - 2


ENV_FILE = env.str("ENV_FILE", default=ROOT_DIR(".env"))
if os.path.exists(ENV_FILE):
    environ.Env.read_env(ENV_FILE)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY", default="default")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])


# Application definition

INSTALLED_APPS = [
    'osschallenge.apps.OsschallengeConfig',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'easy_thumbnails',
    'django_markdown',
]

MARKDOWN_EXTENSIONS = 'extra', 'codehilite'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'osschallenge.urls'

'''
THUMBNAIL_ALIASES = {
    {target}: {
        {alias name}: {'size': {(width, height)}, 'crop': {True|'smart'|(x-axis, y-axis)}, 'upscale':{True|False}},
    },
}
'''

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (350, 350), 'crop': 'smart', 'upscale': True},
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'osschallenge.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": env.str("DATABASE_NAME", default="oss_challenge"),
        "USER": env.str("DATABASE_USER", default="osschallenge"),
        "PASSWORD": env.str("DATABASE_PASSWORD", default="osschallenge"),
        "HOST": env.str("DATABASE_HOST", default="postgres"),
        "PORT": env.str("DATABASE_PORT", default="5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en-us', 'English'),
    ('de', 'German'),
)

LOCALE_PATHS = (
    '/home/jonas/gitty/work/oss-challenge.src/oss_challenge/osschallenge/locale',
)

TIME_ZONE = 'Europe/Zurich'

SITE_URL = env.str("SITE_URL", default="http://localhost:8000")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Login redirects to

LOGIN_REDIRECT_URL = '/tasks/'

# Mailserver login settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")
EMAIL_HOST = env.str("EMAIL_HOST", default="mailcatcher")
EMAIL_PORT = env.int("EMAIL_PORT", default=1025)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=False)
DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", default="osschallenge@oss-challenge.ch")


STATIC_ROOT = os.path.join(BASE_DIR, "osschallenge/static")

MEDIA_ROOT = os.path.join(BASE_DIR, "osschallenge/pictures")
MEDIA_URL = '/media/'
