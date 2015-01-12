"""
Django settings for cybots project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

#########################################################
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#########################################################

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APP_ROOT = os.path.dirname(os.path.dirname(__file__))
PROJ_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PUBLIC_ROOT = os.path.abspath(os.path.join(PROJ_ROOT, 'public'))

#########################################################
# Quick-start development settings - unsuitable for production
#########################################################

# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-76d502i&85dp#-g%&+g*5^%m3rk3+j020((-^^k0(7tta303y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

SITE_ID = 1

#########################################################
# Template
#########################################################

# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# )

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.media',
#     'django.core.context_processors.request',
#     'django.core.context_processors.static',
#     'django.core.context_processors.tz',
#     'django.contrib.messages.context_processors.messages',
# )

TEMPLATE_DIRS = (
    os.path.join(PROJ_ROOT, 'templates'),
)

#########################################################
# Application definition
#########################################################

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'mongoengine.django.mongo_auth',
    'cybots.blogs',
    'cybots.news',
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

ROOT_URLCONF = 'cybots.urls'

WSGI_APPLICATION = 'cybots.wsgi.application'


#########################################################
# Database
#########################################################

# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)
AUTH_USER_MODEL = 'mongo_auth.MongoUser'
MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'
SESSION_ENGINE = 'mongoengine.django.sessions'
SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'

MONGO_DB = 'news'
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
from mongoengine import connect
connect(
    MONGO_DB,
    username='adminnews',
    password='news',
    host=MONGO_HOST,
    port=MONGO_PORT
)

#########################################################
# Static files (CSS, JavaScript, Images)
#########################################################
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

STATICFILES_DIRS = (
    os.path.join(PROJ_ROOT, 'static'),
)

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )


#########################################################
# Logging
#########################################################
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         }
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'django.utils.log.NullHandler',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['require_debug_false'],
#             'include_html': True,
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.db.backends': {
#             'handlers': ['null'],
#             'level': 'DEBUG',
#         },
#         'py.warnings': {
#             'handlers': ['null'],
#             'level': 'WARNING',
#             'propagate': False,
#         }
#     }
# }
