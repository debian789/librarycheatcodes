from django.conf.urls import patterns, url

urlpatterns = patterns ('apps.prueba.views',
	url(r'^prueba/$','views_prueba', name = 'prueba'),
)
