# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import RequestContext
from models import *
from forms import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



def view_agregar_proyecto(request):
	if request.user.is_authenticated():
		try: 
			usuario = get_object_or_404(User, id=request.user.id)
		except Http404:
			return HttpResponseRedirect(reserve('proyectos'))

		if request.method == "POST":
			contenidoForm = frm_proyectos(usuario,request.POST,request.FILES)
			if contenidoForm.is_valid:
				contenidoForm.save()
				return HttpResponseRedirect(reverse('proyectos'))
				#return reverse('proyectos')


		formulario = frm_proyectos(usuario)
		contexto = {'formulario':formulario}

		return render(request,'proyectos_ingresar.html',contexto)


def view_proyectos(request):
	if request.method == 'POST':
		formularioBusqueda = frm_proyectos_busqueda(request.POST)
		if formularioBusqueda.is_valid():
			usuario = User.objects.select_related().get(id=request.user.id)
			proyectos = mdl_proyectos.objects.select_related().filter(usuario=usuario)

			if formularioBusqueda.cleaned_data['busqueda']:
				proyectos = proyectos.filter(nombre__icontains=formularioBusqueda.cleaned_data['busqueda'])
			else:
				pass

			if formularioBusqueda.cleaned_data['lenguaje']  :
				proyectos = proyectos.filter(lenguaje=formularioBusqueda.cleaned_data['lenguaje'])
			else:
				pass

			if formularioBusqueda.cleaned_data['interfaz']  :
				proyectos = proyectos.filter(interfaz=formularioBusqueda.cleaned_data['interfaz'])
			else:
				pass

			if formularioBusqueda.cleaned_data['Nivel']  :
				proyectos = proyectos.filter(Nivel=formularioBusqueda.cleaned_data['Nivel'])
			else:
				pass
			if formularioBusqueda.cleaned_data['os']  :
				proyectos = proyectos.filter(os=formularioBusqueda.cleaned_data['os'])
			else:
				pass

			if formularioBusqueda.cleaned_data['adjunto']:
				proyectos = proyectos.filter(archivo__isnull=False).exclude(archivo__exact='')
				#proyectos = proyectos.filter(archivo__isnull=formularioBusqueda.cleaned_data['adjunto'])
				print "busqueda por adjunto "
			else:
				pass


			paginator = Paginator(proyectos,10)
			page = request.POST.get('page')

			try:
				contacts = paginator.page(page)
			except PageNotAnInteger:
				contacts = paginator.page(1)
			except EmptyPage:
				contacts = paginator.page(paginator.num_pages)

			porFormulario=True

			contexto = {"proyectos":contacts,"formularioBusqueda":formularioBusqueda,"porFormulario":porFormulario}
		else:
			usuario = User.objects.select_related().get(id=request.user.id)
			proyectos = mdl_proyectos.objects.select_related().filter(usuario=usuario)
			formularioBusqueda = frm_proyectos_busqueda()

			paginator = Paginator(proyectos,10)

			page = request.POST.get('page')

			try:
				contacts = paginator.page(page)
			except PageNotAnInteger:
				contacts = paginator.page(1)
			except EmptyPage:
				contacts = paginator.page(paginator.num_pages)

			porFormulario=True
			contexto = {"proyectos":contacts,"formularioBusqueda":formularioBusqueda,"porFormulario":porFormulario}

		
		return render(request,"proyectos.html",contexto)

	#contexto = {"proyectos":proyectos}
	else:
		usuario = User.objects.select_related().get(id=request.user.id)
		proyectos = mdl_proyectos.objects.select_related().filter(usuario=usuario)


		formularioBusqueda = frm_proyectos_busqueda()

		paginator = Paginator(proyectos,10)

		page = request.GET.get('page')

		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		contexto = {"proyectos":contacts,"formularioBusqueda":formularioBusqueda}
		
		return render(request,"proyectos.html",contexto)
	#return render_to_response("proyectos.html",contexto,context_instance = RequestContext(request))


def editar_proyecto_view(request,id_proyecto):
	if request.user.is_authenticated():
		try: 
			usuario = get_object_or_404(User, id=request.user.id)
		except Http404:
			return HttpResponseRedirect(reserve('proyectos'))

		try:
			datos= mdl_proyectos.objects.get(id=id_proyecto)
		except mdl_proyectos.DoesNotExist:
			return HttpResponseRedirect(reserve('proyectos'))

		if request.method == "POST":
			contenidoForm = frm_proyectos(usuario,request.POST,request.FILES,instance=datos)
			if contenidoForm.is_valid():
				contenidoForm.save()
				return HttpResponseRedirect('/proyectos')

		

		formulario = frm_proyectos(usuario,instance = datos )
		contexto = {'formulario':formulario}
		return render(request,'proyectos_ingresar.html',contexto)

def single_proyecto_view(request,id_proyecto):
	usuario = User.objects.select_related().get(id=request.user.id)
	proyecto = mdl_proyectos.objects.select_related().filter(usuario=usuario).get(id=id_proyecto)
	contexto = {"proyecto":proyecto}		
	return render(request,"proyectos_detalles.html",contexto)

#def proyecto_uno_view(request,id_proyecto):

def eliminiar_proyecto_view(request,id_proyecto):
	if request.user.is_authenticated():
		usuario = User.objects.select_related().get(id=request.user.id)
		proyecto = mdl_proyectos.objects.select_related().filter(usuario=usuario).get(id=id_proyecto)
		proyecto.delete()
		return HttpResponseRedirect(reverse("proyectos"))
	
	return HttpResponseRedirect(reverse('inicio'))