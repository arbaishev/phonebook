from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'addressbook',
        'USER': 'addressbookuser',
        'PASSWORD': 'addressbookuserpass',
        'HOST': 'localhost',
        'PORT': '',
    }
}
