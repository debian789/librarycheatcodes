from django.conf.urls import patterns, url
#from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns ('apps.codigos.views',
	url(r'^codigos/$','codigos_view', name = 'codigos'),
	url(r'^add/codigo/$','view_agregar_codigo', name = 'agregar_codigo'),
	url(r'^detalle/codigo/(?P<id_codigo>.*)/$','single_codigo',name='detalle_codigo'),

	#url(r'^add/articulo2/$','add_articulos_view2', name = 'vista_articulo_ingresar2'),
	#url(r'^articulo/(?P<id_articulo>.*)/$','single_articulo_view', name = 'vista_articulo'),

)

#if settings.DEBUG:
#    urlpatterns += patterns('django.contrib.staticfiles.views',
#        url(r'^static/(?P<path>.*)$', 'serve'),

#     )



#urlpatterns += staticfiles_urlpatterns()
