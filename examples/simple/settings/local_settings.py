# Django settings for resato_portal project.
import os

from .core import PROJECT_DIR

DEBUG = True
DEBUG_TOOLBAR = not True
# TEMPLATE_DEBUG = DEBUG
DEBUG_TEMPLATE = DEBUG
DEV = True

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': PROJECT_DIR(os.path.join('..', '..', 'db', 'example.db')),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
    }
}

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = PROJECT_DIR(os.path.join('..', '..', 'tmp'))

DEFAULT_FROM_EMAIL = '<no-reply@example.com>'

ADMIN_TIMELINE_NUMBER_OF_ENTRIES_PER_PAGE = 4

os.environ.setdefault(
    'ADMIN_TIMELINE_SOURCE_PATH',
    '/home/foreverchild/bbrepos/django_admin_timeline/src'
)

FIREFOX_BIN_PATH = '/usr/lib/firefox47/firefox'
PHANTOM_JS_EXECUTABLE_PATH = ''
