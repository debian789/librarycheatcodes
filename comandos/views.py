from django.shortcuts import render_to_response,get_object_or_404,render,redirect
from django.template import RequestContext
from django.db.models import Q
from models import mdl_comandos,instruccion_mdl
from forms import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


@login_required
def view_agregar_comando(request):
	try: 
		usuario = get_object_or_404(User, id=request.user.id)
	except Http404:
		return redirect('comandos')

	if request.method == "POST":
		contenidoForm = frm_comandos(usuario,request.POST,request.FILES)
		if contenidoForm.is_valid:
			contenidoForm.save()
			return redirect('comandos')


	formulario = frm_comandos(usuario)
	contexto = {'formulario':formulario,'mensaje':'Nuevo Comando '}

	return render(request,'comandos_ingresar.html',contexto)

@login_required
def view_comandos(request):
	if request.method == 'POST':
		formularioBusqueda = frm_comandos_busqueda(request.POST)
		if formularioBusqueda.is_valid():
			usuario = User.objects.select_related().get(id=request.user.id)
			comandos = mdl_comandos.objects.select_related().filter(usuario=usuario).order_by('-id')

			if formularioBusqueda.cleaned_data['busqueda']:
				comandos = comandos.filter( Q(nombre__icontains=formularioBusqueda.cleaned_data['busqueda'])| Q(comando__icontains=formularioBusqueda.cleaned_data['busqueda'] ))

			paginator = Paginator(comandos,50)
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
			comandos = mdl_comandos.objects.select_related().filter(usuario=usuario).order_by('-id')
			formularioBusqueda = frm_comandos_busqueda()

			paginator = Paginator(comandos,50)

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

	else:
		usuario = User.objects.select_related().get(id=request.user.id)
		#comandos = []#mdl_comandos.objects.select_related().filter(usuario=usuario)
		comandos = mdl_comandos.objects.select_related().filter(usuario=usuario).order_by('-id')
		formularioBusqueda = frm_comandos_busqueda()
		paginator = Paginator(comandos,50)
		page = request.GET.get('page')

		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		contexto = {"comandos":contacts,"formularioBusqueda":formularioBusqueda}		
		return render(request,"comandos.html",contexto)









def view_comandos_publicos(request):
	if request.method == 'POST':
		formularioBusqueda = frm_comandos_busqueda(request.POST)
		if formularioBusqueda.is_valid():
			#usuario = User.objects.select_related().get(id=request.user.id)
			comandos = mdl_comandos.objects.select_related().filter(estado=True).order_by('-id')

			if formularioBusqueda.cleaned_data['busqueda']:
				comandos = comandos.filter( Q(nombre__icontains=formularioBusqueda.cleaned_data['busqueda'])| Q(comando__icontains=formularioBusqueda.cleaned_data['busqueda'] ))

			paginator = Paginator(comandos,50)
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
			#usuario = User.objects.select_related().get(id=request.user.id)
			comandos = mdl_comandos.objects.select_related().filter(estado=True).order_by('-id')
			formularioBusqueda = frm_comandos_busqueda()

			paginator = Paginator(comandos,50)

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

	else:
		#usuario = User.objects.select_related().get(id=request.user.id)
		#comandos = []#mdl_comandos.objects.select_related().filter(usuario=usuario)
		comandos = mdl_comandos.objects.select_related().filter(estado=True).order_by('-id')
		formularioBusqueda = frm_comandos_busqueda()
		paginator = Paginator(comandos,50)
		page = request.GET.get('page')

		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		contexto = {"comandos":contacts,"formularioBusqueda":formularioBusqueda}		
		return render(request,"comandos.html",contexto)










@login_required
def view_editar_comando(request,id_comando):
	try: 
		usuario = get_object_or_404(User, id=request.user.id)
	except Http404:
		return redirect('comandos')

	try:
		datos= mdl_comandos.objects.get(id=id_comando)
	except mdl_comandos.DoesNotExist:
		return redirect('comandos')

	if request.method == "POST":
		contenidoForm = frm_comandos(usuario,request.POST,request.FILES,instance=datos)
		if contenidoForm.is_valid():
			contenidoForm.save()
			return redirect('comandos')

	

	formulario = frm_comandos(usuario,instance = datos )
	contexto = {'formulario':formulario ,'mensaje':'Editar Comando  '}
	return render(request,'comandos_ingresar.html',contexto)

@login_required
def view_comando_simple(request,id_comando):
	usuario = User.objects.select_related().get(id=request.user.id)
	try: 
		comando = mdl_comandos.objects.select_related().filter(usuario=usuario).get(id=id_comando)

		intrucciones = instruccion_mdl.objects.filter(comando=comando)
		print intrucciones


	except mdl_comandos.DoesNotExist:
		return redirect('inicio')

	contexto = {"comando":comando,"intrucciones":intrucciones}		
	return render(request,"comandos_detalles.html",contexto)

def view_comando_simple_publico(request,id_comando):
	try: 
		comando = mdl_comandos.objects.select_related().filter(estado=True).get(id=id_comando)
	except mdl_comandos.DoesNotExist:
		return redirect('inicio')
	#usuario = User.objects.select_related().get(id=request.user.id)
	#comando = mdl_comandos.objects.select_related().filter(usuario=usuario).get(id=id_comando)
	contexto = {"comando":comando}		
	return render(request,"comandos_detalles.html",contexto)


@login_required
def view_eliminar_comando(request,id_comando):
	usuario = User.objects.select_related().get(id=request.user.id)
	comando = mdl_comandos.objects.select_related().filter(usuario=usuario).get(id=id_comando)
	comando.delete()
	return redirect("comandos")	
	# return redirect('inicio')