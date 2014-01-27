from django.shortcuts import render_to_response,get_object_or_404,render,Http404
from django.template import RequestContext
from apps.codigos.models import *
from apps.codigos.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.contrib.auth.models import User


from django.utils.html import escape
from pygments.lexers import LEXERS

def codigos_view(request):
	if request.method == 'POST':
		formularioBusqueda = frm_codigos_busqueda(request.POST)
		if formularioBusqueda.is_valid():
			usuario = User.objects.select_related().get(id=request.user.id)
			codigos = mdl_codigos.objects.select_related().filter(usuario=usuario)

			if formularioBusqueda.cleaned_data['busqueda']:
				codigos = codigos.filter(titulo__icontains=formularioBusqueda.cleaned_data['busqueda'])
			else:
				pass

			if formularioBusqueda.cleaned_data['lenguaje']  :
				codigos = codigos.filter(lenguaje=formularioBusqueda.cleaned_data['lenguaje'])
			else:
				pass

			if formularioBusqueda.cleaned_data['adjunto']:
				codigos = codigos.filter(archivo__isnull=False).exclude(archivo__exact='')
				#codigos = codigos.filter(archivo__isnull=formularioBusqueda.cleaned_data['adjunto'])
				print "busqueda por adjunto "
			else:
				pass


			paginator = Paginator(codigos,10)
			page = request.POST.get('page')

			try:
				contacts = paginator.page(page)
			except PageNotAnInteger:
				contacts = paginator.page(1)
			except EmptyPage:
				contacts = paginator.page(paginator.num_pages)

			porFormulario=True

			contexto = {"codigos":contacts,"formularioBusqueda":formularioBusqueda,"porFormulario":porFormulario}
		else:
			usuario = User.objects.select_related().get(id=request.user.id)
			codigos = mdl_codigos.objects.select_related().filter(usuario=usuario)
			formularioBusqueda = frm_codigos_busqueda()

			paginator = Paginator(codigos,10)

			page = request.POST.get('page')

			try:
				contacts = paginator.page(page)
			except PageNotAnInteger:
				contacts = paginator.page(1)
			except EmptyPage:
				contacts = paginator.page(paginator.num_pages)

			porFormulario=True
			contexto = {"codigos":contacts,"formularioBusqueda":formularioBusqueda,"porFormulario":porFormulario}

		
		return render(request,"codigos.html",contexto)

	#contexto = {"codigos":codigos}
	else:
		usuario = User.objects.select_related().get(id=request.user.id)
		codigos = mdl_codigos.objects.select_related().filter(usuario=usuario)


		formularioBusqueda = frm_codigos_busqueda()

		paginator = Paginator(codigos,10)

		page = request.GET.get('page')

		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		contexto = {"codigos":contacts,"formularioBusqueda":formularioBusqueda}
		
		return render(request,"codigos.html",contexto)

def view_agregar_codigo(request):
	if request.user.is_authenticated():
		try: 
			usuario = get_object_or_404(User, id=request.user.id)
		except Http404:
			return HttpResponseRedirect(reserve('codigos'))

		if request.method == "POST":
			contenidoForm = frm_codigos(usuario,request.POST,request.FILES)
			if contenidoForm.is_valid():
				contenidoForm.save()
				return HttpResponseRedirect('/codigos')

		formulario = frm_codigos(usuario)
		contexto = {'formulario':formulario}
		#return render_to_response('codigos/codigo_ingresar.html',contexto,context_instance=RequestContext(request))
		return render(request,'codigo_ingresar.html',contexto)
	else:
		return HttpResponseRedirect('/codigos/')

def editar_codigo_view(request,id_codigo):
	if request.user.is_authenticated():
		try: 
			usuario = get_object_or_404(User, id=request.user.id)
		except Http404:
			return HttpResponseRedirect(reserve('codigos'))

		try:
			datos= mdl_codigos.objects.get(id=id_codigo)
		except mdl_codigos.DoesNotExist:
			return HttpResponseRedirect(reserve('codigos'))

		if request.method == "POST":
			contenidoForm = frm_codigos(usuario,request.POST,request.FILES,instance=datos)
			if contenidoForm.is_valid():
				contenidoForm.save()
				return HttpResponseRedirect('/codigos')


		formulario = frm_codigos(usuario,instance = datos )
		contexto = {'formulario':formulario}
		return render(request,'codigo_ingresar.html',contexto)

def eliminiar_codigo_view(request,id_codigo):
	if request.user.is_authenticated():
		datos = mdl_codigos.objects.get(id=id_codigo)
		datos.delete()
		return HttpResponseRedirect('/codigos')

	return HttpResponseRedirect('/')


def filtroBusqueda(request):
	pass


def single_codigo(request,id_codigo):
	if request.method == 'POST':
		formularioBusqueda = frm_codigos_busqueda(request.POST)
		codigosBuequeda = mdl_codigos.objects.filter(titulo= formularioBusqueda.cleaned_data['buesqueda'])
		contexto = {"codigos":codigosBuequeda,"formularioBusqueda":formularioBusqueda}
		return render(request,"codigos.html",contexto)
	else:
		formularioBusqueda = frm_codigos_busqueda()
		codigo = mdl_codigos.objects.get(id=id_codigo)
		codigoFuente = '<pre lang="'+ escape(codigo.lenguaje) +'">' + escape(codigo.codigo) + '</pre>' 

		contexto = {"codigo":codigo,"formularioBusqueda":formularioBusqueda,"codigoFuente":codigoFuente}
		return render(request,'codigo_detalles.html',contexto)


from django.views.generic import ListView, DetailView


class CodigosListView(ListView):
	model = mdl_codigos
	context_object_name = 'codigos'
	def get_template_names(self):
		return 'codigos.html'

class CodigosDetailView(DetailView):
	model = mdl_codigos
	def get_template_names(self):
		return 'codigos.html'


from apps.codigos.serializers import  codigosSerializer,lenguajeSerializer,soSerializer
from rest_framework import viewsets
from apps.elementos_comunes.models import *


class CodigosViewSet(viewsets.ModelViewSet):
	queryset = mdl_codigos.objects.all()
	serializer_class = codigosSerializer

class LenguajeViewSet(viewsets.ModelViewSet):
	queryset = mdl_lenguaje.objects.all()
	serializer_class = lenguajeSerializer

class SoViewSet(viewsets.ModelViewSet):
	queryset = mdl_sistema_operativo.objects.all()
	serializer_class = soSerializer


