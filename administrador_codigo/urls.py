from django.conf.urls import patterns, include, url
from rest_framework import routers
from apps.codigos.views import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'codigos',CodigosViewSet)
router.register(r'leguaje',LenguajeViewSet)


urlpatterns = patterns('',
    url(r'^api/',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^',include('apps.home.urls')),
    url(r'^',include('apps.codigos.urls')),
    url(r'^',include('apps.proyectos.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),


    
    # Examples:
    # url(r'^$', 'administrador_codigo.views.home', name='home'),
    # url(r'^administrador_codigo/', include('administrador_codigo.foo.urls')),
    #url(r'^',include('apps.prueba.urls')),
    #url(r'^',include('apps.proyectos.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:


)
