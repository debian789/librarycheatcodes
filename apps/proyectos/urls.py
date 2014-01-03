from django.conf.urls import patterns, url

urlpatterns = patterns ('apps.proyectos.views',
	url(r'^proyectos/$','view_proyectos', name = 'proyectos'),
	url(r'^add/proyecto/$','view_agregar_proyecto', name = 'agregar_proyecto'),
	#url(r'^add/articulo2/$','add_articulos_view2', name = 'vista_articulo_ingresar2'),
	#url(r'^articulo/(?P<id_articulo>.*)/$','single_articulo_view', name = 'vista_articulo'),

)



