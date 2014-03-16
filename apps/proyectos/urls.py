from django.conf.urls import patterns, url

urlpatterns = patterns ('apps.proyectos.views',
	url(r'^proyectos/$','view_proyectos', name = 'proyectos'),
	url(r'^add/proyecto/$','view_agregar_proyecto', name = 'agregar_proyecto'),
	url(r'^proyecto/editar/(?P<id_proyecto>.*)/$','view_editar_proyecto',name='editar_proyecto'),
	url(r'^proyecto/detalles/(?P<id_proyecto>.*)/$','view_proyecto_simple',name='detalle_proyecto'),
	url(r'^proyecto/eliminar/(?P<id_proyecto>.*)/$','view_eliminiar_proyecto',name='eliminar_proyecto'),
	url(r'^proyecto/pdf/(?P<id_proyecto>.*)/$','proyecto_pdf',name='proyecto_pdf'),

)



