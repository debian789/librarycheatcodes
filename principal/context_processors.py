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
        {'name': 'Inicio ', 'url':reverse('inicio_sesion')},
        {'name': 'Mis Comandos ', 'url':reverse('comandos')},
        {'name': 'Mis Codigos ', 'url': reverse('codigos')},        
        {'name': 'Comandos Publicos ', 'url':reverse('comandos_publicos')},
        {'name': 'Codigos Publicos', 'url': reverse('codigos_publicos')},
        #{'name': 'Mis Proyectos ', 'url': reverse('proyectos')},
        #{'name': 'Favoritos', 'url': reverse('proyectos')},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu

def menu_publico(request):
    menu = {'menu_publico': [
        {'name': 'Comandos ', 'url':reverse('comandos_publicos')},
        {'name': 'Codigos ', 'url': reverse('codigos_publicos')},
        #{'name': 'Proyectos ', 'url': reverse('proyectos_publicos')},
        
    ]}
    for item in menu['menu_publico']:
        if request.path == item['url']:
            item['active'] = True
    return menu

