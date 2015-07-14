from django.conf.urls import patterns, url

urlpatterns = patterns(
    'django_pygments.views',
    (r'^demo/$', 'demo'),
)
