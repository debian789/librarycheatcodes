from random import choice 
from principal.models import GoogleAnalytics_mdl

frases = ['hola mundo ','django es lo mejor ','es dominto :P']

def saludar(request):
	return {'saludo':choice(frases)}

from django.core.urlresolvers import reverse


def googleAnalytics(request):
    try:
        data = GoogleAnalytics_mdl.objects.all()
    except GoogleAnalytics_mdl.DoesNotExist:
        return {'AU':'','siteWeb':''}


    return {'googleAnalytics':data}


def menu(request):
    menu = {'menu': [
        {'name': 'Inicio ', 'url':reverse('inicio_sesion'),'icono':'icon-home3'},
        {'name': 'Mis Comandos ', 'url':reverse('comandos'),'icono':'icon-terminal'},
        {'name': 'Mis Codigos ', 'url': reverse('codigos'),'icono':'icon-embed2'},        
        {'name': 'Comandos Publicos ', 'url':reverse('comandos_publicos'),'icono':'icon-terminal'},
        {'name': 'Codigos Publicos', 'url': reverse('codigos_publicos'),'icono':'icon-embed2'},
        {'name': 'Salir', 'url': reverse('salir'),'icono':'icon-exit'},
        #{'name': 'Mis Proyectos ', 'url': reverse('proyectos')},
        #{'name': 'Favoritos', 'url': reverse('proyectos')},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu

def menu_publico(request):
    menu = {'menu_publico': [
        {'name': 'Inicio ', 'url':reverse('inicio'),'icono':'icon-home3'},
        {'name': 'Comandos ', 'url':reverse('comandos_publicos'),'icono':'icon-terminal'},
        {'name': 'Codigos ', 'url': reverse('codigos_publicos'),'icono':'icon-embed2'},
        {'name': 'Ingresar ', 'url':reverse('ingresar'),'icono':'icon-enter'},
        {'name': 'Registrarse ', 'url':reverse('registrar'),'icono':'icon-clipboard'},
        
        #{'name': 'Proyectos ', 'url': reverse('proyectos_publicos')},
        
    ]}
    for item in menu['menu_publico']:
        if request.path == item['url']:
            item['active'] = True
    return menu

