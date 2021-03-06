"""
Django settings for tweetme2 project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
from corsheaders.defaults import default_headers

import rest_framework

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d2x+#lnn)&qdvi*dr4_a#7%m0i)=a9d-^2^u^8bz_85@c4p+vq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.cfe.sh', 'localhost', '127.0.0.1:3000', '127.0.0.1:8000']
# ALLOWED_HOSTS = ['*']
LOGIN_URL = "/login"
TWEET_ACTION_OPTIONS = ["like", "unlike", "retweet"]

MAX_TWEET_LENGTH = 240

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third-party
    "corsheaders",
    'rest_framework',
    # internal
    'tweets',
    'accounts',
    'profiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tweetme2.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'tweetme2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# <React ?????? ??????>
# 1. npm rum build
# 2. react_app build ?????? static ????????? django ???????????? ??????
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
# 3. make dir static-root
# 4. ./manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, "static-root")
# 5. react_app build ?????? ??? index.html??? ???????????? django template??? react ????????? html ????????? ??????


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


CORS_ALLOW_ALL_ORIGINS = True # ?????? ??????????????? ?????? ???????????? ????????? ??? ????????? ??????
CORS_URLS_REGEX = r"^/api/.*$" # ?????? ????????? ???????????? ?????? ?????? ??????
CORS_ALLOW_HEADERS = default_headers + ( 'HTTP_X_REQUESTED_WITH','X-CSRFToken', )


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DEFAULT_RENDERER_CLASSES = [
    'rest_framework.renderers.JSONRenderer',
]


DEFAULT_AUTHENTICATION_CLASSES = [
    'rest_framework.authentication.SessionAuthentication',
]

if DEBUG:
    DEFAULT_RENDERER_CLASSES += [
        'rest_framework.renderers.BrowsableAPIRenderer', ]
    DEFAULT_AUTHENTICATION_CLASSES += [
        'tweetme2.rest_api.dev.DevAuthentication'
    ]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': DEFAULT_AUTHENTICATION_CLASSES,
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES
}
