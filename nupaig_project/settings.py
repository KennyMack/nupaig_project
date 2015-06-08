"""
Django settings for nupaig_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os import path
BASE_DIR = path.dirname(path.dirname(__file__))

PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*y!el^vwa)z6rz8b+c3)s-=9p$((y6ty2_$6k^nhe5jdyux6bq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

LOGIN_URL = 'mordor:login'

LOGOUT_URL = 'mordor:logout'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mordor_app',
    'nupaig_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nupaig_project.urls'

WSGI_APPLICATION = 'nupaig_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bd_nupaig',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_CHARSET = 'utf-8'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Json files path
JSON_ROOT = path.join(PROJECT_ROOT, 'mordor_app/static/json').replace('\\', '/')

# Static files definitions
STATIC_URL = '/static/'

STATIC_ROOT = path.join(PROJECT_ROOT, 'static').replace('\\', '/')

STATICFILES_DIRS = (
    path.join(PROJECT_ROOT, 'nupaig_app/static/'),
    path.join(PROJECT_ROOT, 'mordor_app/static/'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Media files definitions
MEDIA_URL = '/media/'

MEDIA_ROOT = path.join(PROJECT_ROOT, 'nupaig_app/media').replace('\\', '/')


# Template files Definitions
TEMPLATE_DIRS = (
    path.join(PROJECT_ROOT, 'nupaig_app/templates'),
    path.join(PROJECT_ROOT, 'mordor_app/templates'),

)

