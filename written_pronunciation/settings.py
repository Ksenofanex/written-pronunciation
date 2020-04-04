import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # Built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Local apps
    'users.apps.UsersConfig',
    'dictionary.apps.DictionaryConfig',

    # Third-party apps
    'crispy_forms',

    # Allauth for registration.
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Django Rest Framework
    'rest_framework',
    'rest_framework.authtoken', # Built-in token auth. You must add it after adding TokenAuthentication to the bottom.
    'rest_framework_swagger',

    # Django-rest-auth for API login, logout, registration, pass reset etc.
    'rest_auth', # Django-rest-auth for logging in & out and pass reset. You can use it with allauth.
    'rest_auth.registration',
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

ROOT_URLCONF = 'written_pronunciation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # For project-level directory.
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

WSGI_APPLICATION = 'written_pronunciation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static',)]

# User related settings.
AUTH_USER_MODEL = 'users.CustomUser' # Use the CustomUser model instead of default one.


# Authentication
LOGIN_REDIRECT_URL = 'home' # After logging in successfully, redirect to specified url name.
LOGOUT_REDIRECT_URL = 'home' # After logging out successfully, redirect to specified url name.

# Crispy template pack.
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Django Rest Framework settings.
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [  # For aut & authorization. Which users are going to be able to see and what can
        # they do?
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',  # IsAuthenticated, AllowAny etc.
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [  # new
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',  # Important for DOCS. Won't work without it.
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # For pass reset e-mail and account confirmation.

SITE_ID = 1  # For hosting multiple websites. Allauth uses this with django.contrib.sites.

SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_login',
    'LOGOUT_URL': 'rest_logout',
}
