from django.conf.urls import patterns, url

urlpatterns = patterns ('apps.comandos.views',
	url(r'^comandos/$','view_comandos', name = 'comandos'),
	url(r'^add/comando/$','view_agregar_comando', name = 'agregar_comando'),
	url(r'^comandos/editar/(?P<id_comando>.*)/$','view_editar_comando',name='editar_comando'),
	url(r'^comandos/detalles/(?P<id_comando>.*)/$','view_comando_simple',name='detalle_comando'),
	url(r'^comandos/eliminar/(?P<id_comando>.*)/$','view_eliminar_comando',name='eliminar_comando'),
)



