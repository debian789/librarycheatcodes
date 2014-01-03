from random import choice 

frases = ['hola mundo ','django es lo mejor ','es dominto :P']

def saludar(request):
	return {'saludo':choice(frases)}



from django.core.urlresolvers import reverse

def menu(request):
    menu = {'menu': [
        {'name': 'Inicio', 'url': reverse('codigos')},
        {'name': 'Diagramas', 'url': reverse('galeria')},
        {'name': 'Codigos', 'url': reverse('codigos')},
        {'name': 'Proyectos', 'url': reverse('proyectos')},
        {'name': 'Enlaces', 'url': reverse('enlaces')},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu

