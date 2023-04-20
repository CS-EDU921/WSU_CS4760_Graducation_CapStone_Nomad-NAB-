"""
Django settings for DjangoNAB project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from os import path as os_path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=6ct1nwxln$)s9@otmrp&_ksnmwy+s=y+7_$&k%nfpo(cw#px_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# If in development, put your IP address in localhosts
# In React, fetch from http://<IP Adress>:<port>/API/
# when running the server, use 'python manage.py runserver 0.0.0.0:800' or whatever port number you want
# this allows other locally run stuff to access django
#remember to take your ip out before you release this

ALLOWED_HOSTS = [
    '10.0.0.194', # Matt's
    '10.0.0.195',
    '192.168.1.155',
    '10.0.0.141', # Jaden's
    '192.168.1.197', # Jaden's
    '172.18.80.1', # Amanda's
    '172.20.192.63', #Vipen
    '5k4s9m4.croskelley1.19000.exp.direct',
    '192.168.1.135',
    '192.168.1.1',
    '192.168.0.142',
]


# Application definition

INSTALLED_APPS = [
    'NeedABedAPI.apps.NeedabedapiConfig',
    'django_filters',
    'rest_framework',
    'requests',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoNAB.urls'

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

WSGI_APPLICATION = 'DjangoNAB.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os_path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

# Byte key for encrypting the user key in the Demographics table
USER_ID_KEY = b'deFn_-w4EHmdEmAw7a6P9NrLiPHUUiG0tSAdZP2prXE='

# GeoApify key to use the GeoApify service
# If this expires or no longer works, you may get another one from 
# the GeoApify site
GEOAPIFY_KEY = "ae1c21d7d0f54830910f2fe9d75a5889"