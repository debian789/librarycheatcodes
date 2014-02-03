from django.conf.urls import patterns, include, url
from rest_framework import routers
from apps.codigos.views import *
from django.conf import settings


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
    url(r'^',include('apps.comandos.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)
