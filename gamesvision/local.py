from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'blog',
        'USER': "root",
        'PASSWORD': "toor",
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
