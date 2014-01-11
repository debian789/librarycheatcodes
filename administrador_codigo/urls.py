from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^',include('apps.home.urls')),
    url(r'^',include('apps.proyectos.urls')),
    url(r'^',include('apps.codigos.urls')),

    #url(r'^',include('apps.prueba.urls')),
	
    # Examples:
    # url(r'^$', 'administrador_codigo.views.home', name='home'),
    # url(r'^administrador_codigo/', include('administrador_codigo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
