# Django settings for administrador_codigo project.
import os
#RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {var_name} environment variable'
        raise ImproperlyConfigured(error_msg.format(var_name=var_name))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.

        'NAME': 'biblioteca',                      # Or path to database file if using sqlite3.

        #'NAME': 'app-dev',                       # Or path to database file if using sqlite3.
        #'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.

        #'USER': 'user',  #.
        'USER': 'root',
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}




# configuracion para heroku
#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
############################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-CO'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = 'media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = ''
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = ''
#STATIC_ROOT = 'staticfiles'
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['staticfiles'])
STATICFILES_STORAGE ='django.contrib.staticfiles.storage.CachedStaticFilesStorage'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'


# Additional locations of static files
STATICFILES_DIRS = (
   # os.path.join(RUTA_PROYECTO,'static'),

    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)



# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'uz+_yt-4%0s2kwyr3)s9k-k0sl6+p_0ysh8l@4f=eb#%plp23h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'administrador_codigo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'administrador_codigo.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.codigos',
    'mockups',
    'apps.elementos_comunes',
    'apps.django_pygments',
    'apps.comandos',
    'apps.home',
    'rest_framework',
    'django_extensions',
    'social.apps.django_app.default',
    #'django_ace',
    #'data_exports',
    # 'pisa',
    #'rest_framework',
    #'apps.prueba',
    'apps.proyectos',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#permite publicar variables globales en los template
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'apps.home.context_processors.menu',
    'apps.home.context_processors.menu_publico',
    #hablita optener datos de request en los templates  {{ request.get_full_path }}
    'django.core.context_processors.request',
    )


LOGIN_URL = '/login/'

# Python Social Auth

## Twitter

SOCIAL_AUTH_TWITTER_KEY = 'SOCIAL_AUTH_TWITTER_KEY'
SOCIAL_AUTH_TWITTER_SECRET = 'OCIAL_AUTH_TWITTER_SECRET'

#SOCIAL_AUTH_TWITTER_KEY = get_env_variable('SOCIAL_AUTH_TWITTER_KEY')
#SOCIAL_AUTH_TWITTER_SECRET = get_env_variable('SOCIAL_AUTH_TWITTER_SECRET')

##Google


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'

#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_env_variable('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_env_variable('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')




## Facebook
#SOCIAL_AUTH_FACEBOOK_KEY = get_env_variable('SOCIAL_AUTH_FACEBOOK_KEY')
#SOCIAL_AUTH_FACEBOOK_SECRET =  get_env_variable('SOCIAL_AUTH_FACEBOOK_SECRET')
#SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']



# Backends
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.google.GoogleOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOpenId',
    'django.contrib.auth.backends.ModelBackend',
)

# URLs
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/login/'
SOCIAL_AUTH_BACKEND_ERROR_URL= '/'

