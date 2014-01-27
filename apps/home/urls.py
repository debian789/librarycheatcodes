from django.conf.urls import patterns, url

urlpatterns = patterns ('apps.home.views',
	url(r'^inicioSesion/$','inicio_sesion_view', name = 'inicio_sesion'),
	url(r'^$','ingresar_view', name = 'inicio'),
	url(r'^salir/$','salir_view',name='salir'),
	url(r'^ingresar/$','ingresar_view',name="ingresar"),
	url(r'^agregar/favoritos/(?P<id_codigo>.*)/$','agregar_favoritos_view',name='agregar_favorito'),
	url(r'^quitar/favoritos/inicio/(?P<id_codigo>.*)/$','quitar_favoritos_principal_view',name='quitar_fav_princ'),
	url(r'^quitar/favoritos/(?P<id_codigo>.*)/$','quitar_favorito',name='quitar_favorito'),
)


