from random import choice 

frases = ['hola mundo ','django es lo mejor ','es dominto :P']

def saludar(request):
	return {'saludo':choice(frases)}

from django.core.urlresolvers import reverse

def menu(request):
    menu = {'menu': [
        {'name': 'Mis Codigos', 'url': reverse('codigos')},
        {'name': 'Mis Proyectos', 'url': reverse('proyectos')}
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu

