from django.shortcuts import render_to_response,get_object_or_404,render,Http404,redirect
from django.template import RequestContext
from django.db.models import Q
from codigos.models import *
from codigos.forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.html import escape
from pygments.lexers import LEXERS
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template.loader import render_to_string
from django.http import HttpResponse



# def datos(request,id):
# 	return HttpResponse("hola mundo ");

def generar_pdf(html):
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

def codigo_pdf(request,id_codigo):
	if request.user.is_authenticated():
		usuario = User.objects.select_related().get(id=request.user.id)
		codigo = mdl_codigos.objects.select_related().filter(usuario=usuario).get(id=id_codigo)
		codigoFuente = '<pre  lang="'+ escape(codigo.lenguaje) +'">' + escape(codigo.codigo) + '</pre>' 
		html = render_to_string('codigo_pdf.html', {'pagesize':'A4', "codigo":codigo,"codigoFuente":codigoFuente}, context_instance=RequestContext(request))
		return generar_pdf(html)
	else:
		codigo = mdl_codigos.objects.select_related().filter(estado=True).get(id=id_codigo)
		codigoFuente = '<pre  lang="'+ escape(codigo.lenguaje) +'">' + escape(codigo.codigo) + '</pre>' 
		html = render_to_string('codigo_pdf.html', {'pagesize':'A4', "codigo":codigo,"codigoFuente":codigoFuente}, context_instance=RequestContext(request))
		return generar_pdf(html)




@login_required
def view_codigos(request):
	if request.method == 'POST':

		# formulario de busqueda #
		formularioBusqueda = frm_codigos_busqueda(request.POST)
		if formularioBusqueda.is_valid():
			usuario = User.objects.select_related().get(id=request.user.id)
			codigos = mdl_codigos.objects.select_related().filter(usuario=usuario).order_by('-id')
			if formularioBusqueda.cleaned_data['busqueda']:
				codigos = codigos.filter( Q(titulo__icontains=formularioBusqueda.cleaned_data['busqueda']) | Q(descripcion__icontains=formularioBusqueda.cleaned_data['busqueda']) ) 
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

			paginator = Paginator(codigos,20)
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
			codigos = mdl_codigos.objects.select_related().filter(usuario=usuario).order_by('-id')
			formularioBusqueda = frm_codigos_busqueda()

			paginator = Paginator(codigos,20)

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
		#para implementar formulario.media en la plantilla html para el plugin de django-ace#
		codigos = mdl_codigos.objects.select_related().filter(usuario=usuario).order_by('-id')
		formularioBusqueda = frm_codigos_busqueda()
		paginator = Paginator(codigos,20)
		page = request.GET.get('page')
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		contexto = {"codigos":contacts,"formularioBusqueda":formularioBusqueda}		
		return render(request,"codigos.html",contexto)



def view_codigos_publicos(request):
	if request.method == 'POST':
		formularioBusqueda = frm_codigos_busqueda(request.POST)
		if formularioBusqueda.is_valid():
			#usuario = User.objects.select_related().get(id=request.user.id)
			codigos = mdl_codigos.objects.select_related().filter(estado=True).order_by('-id')

			if formularioBusqueda.cleaned_data['busqueda']:
				codigos = codigos.filter( Q(titulo__icontains=formularioBusqueda.cleaned_data['busqueda']) | Q(descripcion__icontains=formularioBusqueda.cleaned_data['busqueda']) ) 
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


			paginator = Paginator(codigos,20)
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
			#usuario = User.objects.select_related().get(id=request.user.id)
			codigos = mdl_codigos.objects.select_related().filter(estado=True).order_by('-id')
			formularioBusqueda = frm_codigos_busqueda()

			paginator = Paginator(codigos,20)

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
		#usuario = User.objects.select_related().get(id=request.user.id)
		codigos = mdl_codigos.objects.select_related().filter(estado=True).order_by('-id')
		formularioBusqueda = frm_codigos_busqueda()
		paginator = Paginator(codigos,20)
		page = request.GET.get('page')
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		contexto = {"codigos":contacts,"formularioBusqueda":formularioBusqueda}		
		return render(request,"codigos.html",contexto)
























@login_required
def view_agregar_codigo(request):
	try: 
		usuario = get_object_or_404(User, id=request.user.id)
	except Http404:
		return redirect('codigos')

	if request.method == "POST":
		contenidoForm = frm_codigos(usuario,request.POST,request.FILES)
		if contenidoForm.is_valid():
			contenidoForm.save()
			return redirect('codigos')

	formulario = frm_codigos(usuario)
	contexto = {'formulario':formulario,'mensaje':'Nuevo Codigo '}
	#return render_to_response('codigos/codigo_ingresar.html',contexto,context_instance=RequestContext(request))
	return render(request,'codigo_ingresar.html',contexto)


@login_required
def view_editar_codigo(request,id_codigo):
	try: 
		usuario = get_object_or_404(User, id=request.user.id)
	except Http404:
		return redirect('codigos')

	try:
		datos= mdl_codigos.objects.get(id=id_codigo)
	except mdl_codigos.DoesNotExist:
		return redirect('codigos')

	if request.method == "POST":
		contenidoForm = frm_codigos(usuario,request.POST,request.FILES,instance=datos)
		if contenidoForm.is_valid():
			contenidoForm.save()
			return redirect('codigos')


	formulario = frm_codigos(usuario,instance = datos )
	contexto = {'formulario':formulario,'mensaje':'Editar codigo '}
	return render(request,'codigo_ingresar.html',contexto)





@login_required
def view_eliminiar_codigo(request,id_codigo):
	datos = mdl_codigos.objects.get(id=id_codigo)
	datos.delete()
	return redirect('codigos')

@login_required
def view_codigo_simple(request,id_codigo):
	usuario = User.objects.select_related().get(id=request.user.id)
	try: 
		codigo = mdl_codigos.objects.select_related().filter(usuario=usuario).get(id=id_codigo)
		#codigo = mdl_codigos.objects.select_related().filter(estado=True).get(id=id_codigo)
	except mdl_codigos.DoesNotExist:
		return redirect('inicio')

	codigoFuente = '<pre  lang="'+ escape(codigo.lenguaje) +'"><code>' + escape(codigo.codigo) + '</code></pre>'
	contexto = {"codigo":codigo,"codigoFuente":codigoFuente}	
	return render(request,"codigo_detalles.html",contexto)
	# if request.method == 'POST':
	# 	formularioBusqueda = frm_codigos_busqueda(request.POST)
	# 	codigosBuequeda = mdl_codigos.objects.filter(titulo= formularioBusqueda.cleaned_data['buesqueda'])
	# 	contexto = {"codigos":codigosBuequeda,"formularioBusqueda":formularioBusqueda}
	# 	return render(request,"codigos.html",contexto)
	# else:
	# 	formularioBusqueda = frm_codigos_busqueda()
	# 	codigo = mdl_codigos.objects.get(id=id_codigo)
	# 	codigoFuente = '<pre  lang="'+ escape(codigo.lenguaje) +'">' + escape(codigo.codigo) + '</pre>' 

	# 	contexto = {"codigo":codigo,"formularioBusqueda":formularioBusqueda,"codigoFuente":codigoFuente}
	# 	return render(request,'codigo_detalles.html',contexto)



def view_codigo_simple_publico(request,id_codigo):
	#usuario = User.objects.select_related().get(id=request.user.id)
	#usuario = get_object_or_404(User, id=request.user.id)
	try: 
		codigo = mdl_codigos.objects.select_related().filter(estado=True).get(id=id_codigo)
	except mdl_codigos.DoesNotExist:
		return redirect('inicio')

	codigoFuente = '<pre  lang="'+ escape(codigo.lenguaje) +'"><code>' + escape(codigo.codigo) + '</code></pre>'
	contexto = {"codigo":codigo,"codigoFuente":codigoFuente}	
	return render(request,"codigo_detalles.html",contexto)




# from django.views.generic import ListView, DetailView

# @login_required
# class CodigosListView(ListView):
# 	model = mdl_codigos
# 	context_object_name = 'codigos'
# 	def get_template_names(self):
# 		return 'codigos.html'

# @login_required
# class CodigosDetailView(DetailView):
# 	model = mdl_codigos
# 	def get_template_names(self):
# 		return 'codigos.html'


from codigos.serializers import  codigosSerializer,lenguajeSerializer,soSerializer
from rest_framework import viewsets
from elementos_comunes.models import *


class CodigosViewSet(viewsets.ModelViewSet):
	queryset = mdl_codigos.objects.all()
	serializer_class = codigosSerializer

class LenguajeViewSet(viewsets.ModelViewSet):
	queryset = mdl_lenguaje.objects.all()
	serializer_class = lenguajeSerializer

class SoViewSet(viewsets.ModelViewSet):
	queryset = mdl_sistema_operativo.objects.all()
	serializer_class = soSerializer


