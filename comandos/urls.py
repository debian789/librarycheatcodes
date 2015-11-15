from django.conf.urls import patterns, url

urlpatterns = patterns ('comandos.views',
	url(r'^comandos/$','view_comandos', name = 'comandos'),
	url(r'^comandos-publicos/$','view_comandos_publicos', name = 'comandos_publicos'),
	url(r'^comando/agregar/$','view_agregar_comando', name = 'agregar_comando'),
	url(r'^comando/agregar-nuevo/(?P<id_comando>.*)/$','view_agregar_comando_nuevo', name = 'agregar_comando_nuevo'),
	url(r'^comando/editar/(?P<id_comando>.*)/$','view_editar_comando',name='editar_comando'),
	url(r'^comandoItem/editar/(?P<id_comandoItem>.*)/(?P<id_comando>.*)/$','view_editar_comandoItem',name='editar_comando_item'),
	url(r'^comando/detalles/(?P<id_comando>.*)/$','view_comando_simple',name='detalle_comando'),
	url(r'^comando-publico/detalles/(?P<id_comando>.*)/$','view_comando_simple_publico',name='detalle_comando_publico'),
	url(r'^comando/eliminar/(?P<id_comando>.*)/$','view_eliminar_comando',name='eliminar_comando'),
	url(r'^comandoItem/eliminar/(?P<id_comando>.*)/(?P<id_comandoItem>.*)/$','view_eliminar_comando_item',name='eliminar_comando_item'),
)
