# -*- coding: utf-8 -*-
from .base import *

DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
} 

DATABASES['default'] =  dj_database_url.config()