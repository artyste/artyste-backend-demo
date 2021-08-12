"""
Django settings for arthology project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import requests

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('ARTHOLOGY_DJANGO')

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('DJANGO') == '0':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['arthology-api.eba-spazchiv.us-east-1.elasticbeanstalk.com', '127.0.0.1', 'arthology.io', 'api.arthology.io', 'app.arthology.io']
EC2_PRIVATE_IP = None
try:
    EC2_PRIVATE_IP = requests.get(
        'http://169.254.169.254/latest/meta-data/local-ipv4',
        timeout=0.01).text
except requests.exceptions.RequestException:
    pass
    print(' @ Arthology - Fail to add EC2 ip on the list')

if EC2_PRIVATE_IP:
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)
    print(' @ Arthology - ALLOWED_HOSTS')
    print(ALLOWED_HOSTS)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'api.apps.ApiConfig',
    'accounts',
    'art',
]

SITE_ID = 1

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

ROOT_URLCONF = 'arthology.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'arthology.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# os.environ.get('ARTHOLOGY_RDS_PASS')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'arthologyrds',
        'PASSWORD': os.environ.get('ARTHOLOGY_RDS_PASS'),
        'HOST': 'aari593mi3bwct.cs2cibp8vxrp.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'admin@arthology.io'
EMAIL_HOST_PASSWORD = 'RG8UpVWag6TY0k1P'
EMAIL_USE_TLS = True

CORS_ALLOW_ALL_ORIGINS = True
#
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://app.arthology.io",
# ]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'accounts.UserAccount'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# S3 BUCKETS CONFIG



AWS_ACCESS_KEY_ID = os.environ.get('ARTHOLOGY_AWS_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('ARTHOLOGY_AWS_KEY')
AWS_STORAGE_BUCKET_NAME = 'arthology-files'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_DEFAULT_ACL = 'authenticated-read'
# SECURE_REFERRER_POLICY = 'same-origin'

AWS_S3_ADDRESSING_STYLE = "virtual"

STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}
DOMAIN = ('localhost:3000')
SITE_NAME = ('Arthology')
DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create': 'accounts.serializers.UserCreateSerializer',
        'user': 'accounts.serializers.UserCreateSerializer',
        'current_user': 'accounts.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    }
}

