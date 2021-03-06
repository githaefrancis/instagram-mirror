"""
Django settings for instagram_mirror project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from email.policy import default
from pathlib import Path
import django_heroku
import dj_database_url
from decouple import config,Csv 
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-_#fu2as)5zdigdoix-5q(c6c-l_o)y4la+t34=@y^nyc757!n8'
SECRET_KEY=config("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG',False)


ALLOWED_HOSTS = config('ALLOWED_HOSTS',cast=Csv())


# Application definition

INSTALLED_APPS = [
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'images',
    'user_profile',
    'django_bootstrap5',
    'fontawesome_5',
]

ACCOUNT_ACTIVATION_DAYS=1
REGISTRATION_AUTO_LOGIN=True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'instagram_mirror.urls'
LOGIN_REDIRECT_URL='home'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'instagram_mirror.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

MODE=config("MODE",default="dev")

if config('MODE')=="dev":
    DATABASES={

        'default':{
            'ENGINE':'django.db.backends.postgresql',
            'NAME':config('DB_NAME'),
            'USER':config('DB_USER'),
            'PASSWORD':config('DB_PASSWORD'),
            'HOST':config('DB_HOST'),
            'PORT':'',

        }

    }
else:
    DATABASES={
        'default':dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }

db_from_env=dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

EMAIL_USE_TLS=config('EMAIL_USE_TLS')
EMAIL_HOST=config('EMAIL_HOST')
EMAIL_PORT=config('EMAIL_PORT')
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL='instagrammirrorpro@gmail.com'

STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


AUTH_USER_MODEL='user_profile.CustomUser'
django_heroku.settings(locals())
