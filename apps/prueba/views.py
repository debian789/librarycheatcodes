from django.shortcuts import render
from django.template import RequestContext



#Create your views here.
def views_prueba(request):
	contexto = {"saludo":"Hola mundo"}
	return render (request,"prueba.html",contexto)

# from django.views.generic import ListView, DetailView

# class views_prueba(ListView):
# 	#model = mdl_codigos
# 	context_object_name = {"saludo":"Hola mundo"}
# 	def get_template_names(self):
# 		return 'prueba.html'
