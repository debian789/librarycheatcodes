# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import RequestContext
from models import *
from forms import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage



def view_agregar_proyecto(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			contenidoForm = frm_proyectos(request.POST,request.FILES)
			if contenidoForm.is_valid:
				contenidoForm.save()
				return HttpResponseRedirect('/proyectos/1')


		formulario = frm_proyectos()
		contexto = {'formulario':formulario}

		return render(request,'proyectos_ingresar.html',contexto)


def view_proyectos(request):
	proyectos = mdl_proyectos.objects.filter(publicado=True)
	contexto = {"proyectos":proyectos}
	return render(request,"proyectos.html",contexto)