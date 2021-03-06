# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404,render,redirect
from django.template import RequestContext
from django.db.models import Q
from models import *
from forms import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required



import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template.loader import render_to_string
from django.http import HttpResponse

def generar_pdf(html):
    # Funcion para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

def proyecto_pdf(request,id_proyecto):
	if request.user.is_authenticated():			
		usuario = User.objects.select_related().get(id=request.user.id)
		#def libro_pdf(request, id):
		proyecto = mdl_proyectos.objects.select_related().filter(usuario=usuario).get(id=id_proyecto)
		contexto = {"proyecto":proyecto}
		html = render_to_string('proyecto_pdf.html', {'pagesize':'A4', 'proyecto':proyecto}, context_instance=RequestContext(request))
		return generar_pdf(html)
	else:
		#usuario = User.objects.select_related().get(id=request.user.id)
		#def libro_pdf(request, id):
		proyecto = mdl_proyectos.objects.select_related().filter(estado=True).get(id=id_proyecto)
		contexto = {"proyecto":proyecto}
		html = render_to_string('proyecto_pdf.html', {'pagesize':'A4', 'proyecto':proyecto}, context_instance=RequestContext(request))
		return generar_pdf(html)



@login_required
def view_agregar_proyecto(request):
	try: 
		usuario = get_object_or_404(User, id=request.user.id)
	except Http404:
		return redirect('proyectos')

	if request.method == "POST":
		contenidoForm = frm_proyectos(usuario,request.POST,request.FILES)
		if contenidoForm.is_valid:
			contenidoForm.save()
			return redirect('proyectos')
			#return reverse('proyectos')


	formulario = frm_proyectos(usuario)
	contexto = {'formulario':formulario,'mensaje':'Nuevo Proyecto '}

	return render(request,'proyectos_ingresar.html',contexto)

@login_required
def view_proyectos(request):
	if request.method == 'POST':
		formularioBusqueda = frm_proyectos_busqueda(request.POST)
		if formularioBusqueda.is_valid():
			usuario = User.objects.select_related().get(id=request.user.id)
			proyectos = mdl_proyectos.objects.select_related().filter(usuario=usuario).order_by('-id')

			if formularioBusqueda.cleaned_data['busqueda']:
				proyectos = proyectos.filter( Q(nombre__icontains=formularioBusqueda.cleaned_data['busqueda']) | Q(descripcion__icontains=formularioBusqueda.cleaned_data['busqueda']) )
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
			proyectos = mdl_proyectos.objects.select_related().filter(usuario=usuario).order_by('-id')
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
		proyectos = mdl_proyectos.objects.select_related().filter(usuario=usuario).order_by('-id')


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

def view_proyectos_publicos(request):
	if request.method == 'POST':
		formularioBusqueda = frm_proyectos_busqueda(request.POST)
		if formularioBusqueda.is_valid():
			#usuario = User.objects.select_related().get(id=request.user.id)
			proyectos = mdl_proyectos.objects.select_related().filter(estado=True).order_by('-id')

			if formularioBusqueda.cleaned_data['busqueda']:
				proyectos = proyectos.filter( Q(nombre__icontains=formularioBusqueda.cleaned_data['busqueda']) | Q(descripcion__icontains=formularioBusqueda.cleaned_data['busqueda']) )
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
			#usuario = User.objects.select_related().get(id=request.user.id)
			proyectos = mdl_proyectos.objects.select_related().filter(estado=True).order_by('-id')
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
		#usuario = User.objects.select_related().get(id=request.user.id)
		proyectos = mdl_proyectos.objects.select_related().filter(estado=True).order_by('-id')


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





@login_required
def view_editar_proyecto(request,id_proyecto):
	try: 
		usuario = get_object_or_404(User, id=request.user.id)
	except Http404:
		return redirect('proyectos')

	try:
		datos= mdl_proyectos.objects.get(id=id_proyecto)
	except mdl_proyectos.DoesNotExist:
		return redirect('proyectos')

	if request.method == "POST":
		contenidoForm = frm_proyectos(usuario,request.POST,request.FILES,instance=datos)
		if contenidoForm.is_valid():
			contenidoForm.save()
			return redirect('proyectos')

	formulario = frm_proyectos(usuario,instance = datos )
	contexto = {'formulario':formulario,'mensaje':'Editar Proyecto '}
	return render(request,'proyectos_ingresar.html',contexto)

@login_required
def view_proyecto_simple(request,id_proyecto):
	usuario = User.objects.select_related().get(id=request.user.id)
	try:
		proyecto = mdl_proyectos.objects.select_related().filter(usuario=usuario).get(id=id_proyecto)
	except mdl_proyectos.DoesNotExist:
		return redirect('inicio')

	contexto = {"proyecto":proyecto}		
	return render(request,"proyectos_detalles.html",contexto)



def view_proyecto_simple_publico(request,id_proyecto):
	try:
		proyecto = mdl_proyectos.objects.select_related().filter(estado=True).get(id=id_proyecto)
	except mdl_proyectos.DoesNotExist:
		return redirect('inicio')

	contexto = {"proyecto":proyecto}		
	return render(request,"proyectos_detalles.html",contexto)






@login_required
def view_eliminiar_proyecto(request,id_proyecto):
	usuario = User.objects.select_related().get(id=request.user.id)
	proyecto = mdl_proyectos.objects.select_related().filter(usuario=usuario).get(id=id_proyecto)
	proyecto.delete()
	return redirect("proyectos")