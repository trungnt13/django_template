from cybots.settings.prod import *

TMP_PATH = os.path.abspath(os.path.join(PROJ_ROOT, 'tmp'))

DEBUG = TEMPLATE_DEBUG = True
# SECRET = '42'

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(TMP_PATH, 'db.sqlite3'),
    # }
# }

INTERNAL_IPS = ('127.0.0.1',)

# if 'debug_toolbar' not in INSTALLED_APPS:
    # INSTALLED_APPS += ('debug_toolbar',)

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
