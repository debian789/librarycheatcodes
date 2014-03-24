from django.conf.urls import patterns, include, url

urlpatterns = patterns ('apps.codigos.views',
	url(r'^codigos/$','view_codigos', name = 'codigos'),
	url(r'^codigos-publicos/$','view_codigos_publicos',name='codigos_plublicos'),
	url(r'^codigo/agregar/$','view_agregar_codigo', name = 'agregar_codigo'),
	url(r'^codigo/detalles/(?P<id_codigo>.*)/$','view_codigo_simple',name='detalle_codigo'),
	url(r'^codigo-publico/detalles/(?P<id_codigo>.*)/$','view_codigo_simple_publico',name='detalle_codigo_publico'),
	url(r'^codigo/editar/(?P<id_codigo>.*)/$','view_editar_codigo',name='editar_codigo'),
	url(r'^codigo/eliminar/(?P<id_codigo>.*)/$','view_eliminiar_codigo',name='eliminar_codigo'),
	url(r'^codigo/pdf/(?P<id_codigo>.*)/$','codigo_pdf',name='codigo_pdf'),

)
