"""
Django settings for royaldryfruits project.
"""

from pathlib import Path


# Base Directory

BASE_DIR = Path(__file__).resolve().parent.parent



# Security

SECRET_KEY = 'django-insecure-lqrbcdmm%)gsh2tn32cyjpb($__wp=1l8o@l##mka&yk02f#qn'

DEBUG = True

ALLOWED_HOSTS = []



# Installed Apps

INSTALLED_APPS = [

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',


    # Your App
    'storeapp',

]



# Middleware

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



ROOT_URLCONF = 'royaldryfruits.urls'



# Templates

TEMPLATES = [

    {

        'BACKEND':
        'django.template.backends.django.DjangoTemplates',

        'DIRS':
        [
            BASE_DIR / "templates"
        ],

        'APP_DIRS': True,

        'OPTIONS':
        {

            'context_processors':
            [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]



WSGI_APPLICATION = 'royaldryfruits.wsgi.application'



# Database

DATABASES = {

    'default':
    {

        'ENGINE':
        'django.db.backends.sqlite3',

        'NAME':
        BASE_DIR / 'db.sqlite3',

    }

}



# Password Validation

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]



# Language

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True



# ==========================
# STATIC FILES
# ==========================

STATIC_URL = '/static/'


STATICFILES_DIRS = [

    BASE_DIR / "static",

]


STATIC_ROOT = BASE_DIR / "staticfiles"




# ==========================
# MEDIA FILES (PRODUCT IMAGES)
# ==========================

MEDIA_URL = '/media/'


MEDIA_ROOT = BASE_DIR / "media"




# Authentication

LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "dashboard"

LOGOUT_REDIRECT_URL = "home"




# Email

EMAIL_BACKEND = (
    'django.core.mail.backends.console.EmailBackend'
)




# Default Primary Key

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


RAZORPAY_KEY_ID = "your_key_id"
RAZORPAY_KEY_SECRET = "your_secret_key"