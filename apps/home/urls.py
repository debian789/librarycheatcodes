from django.conf.urls import patterns, url

urlpatterns = patterns ('apps.home.views',
	url(r'^inicioSesion/$','view_inicio_sesion', name = 'inicio_sesion'),
	url(r'^$','view_inicio', name = 'inicio'),
	url(r'^salir/$','view_salir',name='salir'),
	#url(r'^ingresar/$','view_ingresar',name="ingresar"),
	#url(r'^agregar/favorito/(?P<id_codigo>.*)/$','view_agregar_favoritos',name='agregar_favorito'),
	#url(r'^quitar/favorito/inicio/(?P<id_codigo>.*)/$','view_quitar_favorito_principal',name='quitar_fav_princ'),
	#url(r'^quitar/favorito/(?P<id_codigo>.*)/$','view_quitar_favorito',name='quitar_favorito'),
)


