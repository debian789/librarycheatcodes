from django.conf.urls import patterns, url

urlpatterns = patterns ('apps.codigos.views',
	url(r'^codigos/$','codigos_view', name = 'codigos'),
	url(r'^codigos/agregar/$','view_agregar_codigo', name = 'agregar_codigo'),
	url(r'^codigo/detalles/(?P<id_codigo>.*)/$','single_codigo',name='detalle_codigo'),
	url(r'^codigo/editar/(?P<id_codigo>.*)/$','editar_codigo_view',name='editar_codigo'),
	url(r'^codigo/eliminar/(?P<id_codigo>.*)/$','eliminiar_codigo_view',name='eliminar_codigo'),
	#url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,},

)