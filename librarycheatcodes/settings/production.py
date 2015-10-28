# -*- coding: utf-8 -*-
from .base import *

DEBUG = False 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': get_env_variable('nameDB'),
		'USER': get_env_variable('nameUserDB'),
		'PASSWORD': get_env_variable('passUserDB'),
		'HOST': get_env_variable('DATABASE_URL'),

    }
} 

