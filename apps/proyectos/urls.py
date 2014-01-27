from django.conf.urls import patterns, url

urlpatterns = patterns ('apps.proyectos.views',
	url(r'^proyectos/$','view_proyectos', name = 'proyectos'),
	url(r'^add/proyecto/$','view_agregar_proyecto', name = 'agregar_proyecto'),
	url(r'^proyecto/editar/(?P<id_proyecto>.*)/$','editar_proyecto_view',name='editar_proyecto'),
	url(r'^proyecto/detalles/(?P<id_proyecto>.*)/$','single_proyecto_view',name='detalle_proyecto'),
	url(r'^proyecto/eliminar/(?P<id_proyecto>.*)/$','eliminiar_proyecto_view',name='eliminar_proyecto'),
)



