# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import RequestContext
from django.db.models import Q
from models import *
from forms import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



def view_agregar_comando(request):
	if request.user.is_authenticated():
		try: 
			usuario = get_object_or_404(User, id=request.user.id)
		except Http404:
			return HttpResponseRedirect(reserve('comandos'))

		if request.method == "POST":
			contenidoForm = frm_comandos(usuario,request.POST,request.FILES)
			if contenidoForm.is_valid:
				contenidoForm.save()
				return HttpResponseRedirect(reverse('comandos'))
				#return reverse('comandos')


		formulario = frm_comandos(usuario)
		contexto = {'formulario':formulario}

		return render(request,'comandos_ingresar.html',contexto)


def view_comandos(request):
	if request.method == 'POST':
		formularioBusqueda = frm_comandos_busqueda(request.POST)
		if formularioBusqueda.is_valid():
			usuario = User.objects.select_related().get(id=request.user.id)
			comandos = mdl_comandos.objects.select_related().filter(usuario=usuario)

			if formularioBusqueda.cleaned_data['busqueda']:
				comandos = comandos.filter( Q(nombre__icontains=formularioBusqueda.cleaned_data['busqueda'])| Q(comando__icontains=formularioBusqueda.cleaned_data['busqueda'] ))
			else:
				pass

			paginator = Paginator(comandos,10)
			page = request.POST.get('page')

			try:
				contacts = paginator.page(page)
			except PageNotAnInteger:
				contacts = paginator.page(1)
			except EmptyPage:
				contacts = paginator.page(paginator.num_pages)

			porFormulario=True

			contexto = {"comandos":contacts,"formularioBusqueda":formularioBusqueda,"porFormulario":porFormulario}
		else:
			usuario = User.objects.select_related().get(id=request.user.id)
			comandos = mdl_comandos.objects.select_related().filter(usuario=usuario)
			formularioBusqueda = frm_comandos_busqueda()

			paginator = Paginator(comandos,10)

			page = request.POST.get('page')

			try:
				contacts = paginator.page(page)
			except PageNotAnInteger:
				contacts = paginator.page(1)
			except EmptyPage:
				contacts = paginator.page(paginator.num_pages)

			porFormulario=True
			contexto = {"comandos":contacts,"formularioBusqueda":formularioBusqueda,"porFormulario":porFormulario}

		
		return render(request,"comandos.html",contexto)

	#contexto = {"comandos":comandos}
	else:
		usuario = User.objects.select_related().get(id=request.user.id)
		#comandos = []#mdl_comandos.objects.select_related().filter(usuario=usuario)
		comandos = mdl_comandos.objects.select_related().filter(usuario=usuario)



		formularioBusqueda = frm_comandos_busqueda()

		paginator = Paginator(comandos,10)

		page = request.GET.get('page')

		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		contexto = {"comandos":contacts,"formularioBusqueda":formularioBusqueda}

		
		return render(request,"comandos.html",contexto)


def view_editar_comando(request,id_comando):
	if request.user.is_authenticated():
		try: 
			usuario = get_object_or_404(User, id=request.user.id)
		except Http404:
			return HttpResponseRedirect(reserve('comandos'))

		try:
			datos= mdl_comandos.objects.get(id=id_comando)
		except mdl_comandos.DoesNotExist:
			return HttpResponseRedirect(reserve('comandos'))

		if request.method == "POST":
			contenidoForm = frm_comandos(usuario,request.POST,request.FILES,instance=datos)
			if contenidoForm.is_valid():
				contenidoForm.save()
				return HttpResponseRedirect('/comandos')

		

		formulario = frm_comandos(usuario,instance = datos )
		contexto = {'formulario':formulario}
		return render(request,'comandos_ingresar.html',contexto)

def view_comando_simple(request,id_comando):
	usuario = User.objects.select_related().get(id=request.user.id)
	comando = mdl_comandos.objects.select_related().filter(usuario=usuario).get(id=id_comando)
	contexto = {"comando":comando}		
	return render(request,"comandos_detalles.html",contexto)

#def comando_uno_view(request,id_comando):

def view_eliminar_comando(request,id_comando):
	if request.user.is_authenticated():
		usuario = User.objects.select_related().get(id=request.user.id)
		comando = mdl_comandos.objects.select_related().filter(usuario=usuario).get(id=id_comando)
		comando.delete()
		return HttpResponseRedirect(reverse("comandos"))
	
	return HttpResponseRedirect(reverse('inicio'))