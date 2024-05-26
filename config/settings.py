import os
import sys

from datetime import timedelta
from pathlib import Path
from environ import Env

from django.utils.translation import gettext_lazy as _

from doctranslation import __version__


env = Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env_path = os.path.join(BASE_DIR, 'config', '.env')
if os.path.isfile(env_path):
    env.read_env()

# Services
ROOT_DOMAIN = env('ROOT_DOMAIN', default='localhost')
BASE_URL = env('BASE_URL', default='http://localhost:8000')
API_BASE_URL = env('API_BASE_URL', default='http://localhost:8000')
IS_PRODUCTION = ROOT_DOMAIN == 'doc-translation.io'
IS_STAGING = ROOT_DOMAIN == 'doc-translation.dev'
DEBUG = env.bool('DEBUG', default=True)
TESTING = 'test' in sys.argv[1:3] or 'check' in sys.argv[1:3]
VERSION = __version__

# Securities
SECRET_KEY = env('SECRET_KEY', default='django-insecure-d&nj7-#&i@uqwvwz4jdis$_r@09eit=o0(%bss&axu2-265n%b')
ALLOWED_HOSTS = env.list(
    'ALLOWED_HOSTS', default=[
        'localhost',
        '127.0.0.1',
        '[::1]',
    ],
)
CORS_ALLOWED_ORIGINS = env.list(
    'CORS_ALLOWED_ORIGINS', default=[
        'http://127.0.0.1:3000',
        'http://localhost:3000',
    ],
)
CORS_ALLOWED_ORIGIN_REGEXES = env.list(
    'CORS_ALLOWED_ORIGIN_REGEXES', default=[],
)
PASSWORD_HASHERS = env.list(
    'PASSWORD_HASHERS', default=[
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ],
)
CSRF_COOKIE_SECURE = env('CSRF_COOKIE_SECURE', default=False)
CSRF_TRUSTED_ORIGINS = env.list(
    'CSRF_TRUSTED_ORIGINS', default=[
        'http://127.0.0.1:4200',
        'http://localhost:4200',
    ],
)

# WSGI
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
WSGI_APPLICATION = 'config.wsgi.application'
USE_X_FORWARDED_HOST = env.bool('USE_X_FORWARDED_HOST', default=False)

# Application definition
PROJECT_APPS = [
    'doctranslation.modules.authentication',
    'doctranslation.modules.common',
    'doctranslation.modules.translate_agent',
]

PREREQ_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # 3rd-parties
    'corsheaders',
    'django_filters',
    'rest_framework',
]
EXTENDED_APPS = env.list('EXTENDED_APPS', default=['django_extensions'])
INSTALLED_APPS = PROJECT_APPS + PREREQ_APPS + EXTENDED_APPS

# URLs
ROOT_URLCONF = env('ROOT_URLCONF', default='config.urls')

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

# Database
DATABASES = {
    'default': env.db(default='sqlite:///db.sqlite3'),
    'default_replica': env.db(
        'DATABASE_READ_REPLICA_URL',
        default='sqlite:///db.sqlite3',
    ),
}
if TESTING:
    DATABASES['default_replica']['TEST'] = {
        'NAME': DATABASES['default_replica']['NAME'],
        'MIRROR': 'default',
    }

# Auth `django.contrib.auth`
AUTH_USER_MODEL = 'authentication.User'
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
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
)
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = env(
    'STATIC_ROOT',
    default=os.path.join(BASE_DIR, 'static'),
)
STATIC_URL = env('STATIC_URL', default='/static/')
STATICFILES_STORAGE = env(
    'STATICFILES_STORAGE',
    default='django.contrib.staticfiles.storage.StaticFilesStorage',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'dist'),
    os.path.join(BASE_DIR, 'static', 'images'),
)
MEDIA_ROOT = env('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))
MEDIA_URL = env('MEDIA_URL', default='/media/')
DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 15

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE', default='django.core.files.storage.FileSystemStorage')

# REST framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': env.list(
        'DEFAULT_RENDERER_CLASSES',
        default=[
            'doctranslation.serialization.renderers.StatusRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ],
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'EXCEPTION_HANDLER': 'doctranslation.serialization.exception_handler.custom_exception_handler',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
    'COERCE_DECIMAL_TO_STRING': False,
}

# drf-dynamic-fields
DRF_DYNAMIC_FIELDS = {
    'SUPPRESS_CONTEXT_WARNING': True,
}

# django-rest-framework-jwt
JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}
if DEBUG:
    JWT_AUTH['JWT_EXPIRATION_DELTA'] = timedelta(days=1)

# 3rd parties services
GOOGLE_APPLICATION_CREDENTIALS_PATH = env('GOOGLE_APPLICATION_CREDENTIALS_PATH', default=None)
GOOGLE_PROJECT_ID = env('GOOGLE_PROJECT_ID', default=None)
GOOGLE_REGION = env('GOOGLE_REGION', default=None)