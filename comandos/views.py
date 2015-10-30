from django.shortcuts import render_to_response,get_object_or_404,render,redirect
from django.template import RequestContext
from django.db.models import Q
from models import mdl_comandos,instruccion_mdl
from forms import frm_comandos_items,frm_comandos_busqueda,frm_comandos
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
			idRegistro = contenidoForm.save().id 
			if contenidoForm.save().id : 
				idComando = mdl_comandos.objects.get(id=idRegistro)
				itemcomandos = frm_comandos_items(idComando,request.POST,request.FILES)
				if itemcomandos.is_valid: 

					arrayInstruccion = request.POST.getlist('instruccion[]')
					arrayDescripcion = request.POST.getlist('descripcion[]')
					ls_comandos_items = []

					if arrayInstruccion:
						for x in arrayInstruccion:
							ls_comandos_items.append( instruccion_mdl(comando=idComando,instruccion=x,descripcion=arrayDescripcion[0])  )
							if len(arrayDescripcion) > 1:
								del arrayDescripcion[0]
				
						for datos in ls_comandos_items:
							datos.save()

			return redirect('comandos')


	formulario = frm_comandos(usuario)
	comandos_items = frm_comandos_items(1)
	contexto = {'formulario':formulario,'mensaje':'Nuevo Comando ','comandos_items':comandos_items}

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

		
		return render(request,"comandos_publicos.html",contexto)

	else:
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
		return render(request,"comandos_publicos.html",contexto)










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
	return render(request,'comandos_modificar_comando.html',contexto)


@login_required
def view_editar_comandoItem(request,id_comando,id_comandoItem):
	try: 
		comandoId = get_object_or_404(mdl_comandos, usuario=request.user.id,id=id_comando)
		
	except Http404:
		return redirect('comandos')

	try:
		datos= instruccion_mdl.objects.get(id=id_comandoItem,comando=comandoId)
		
	except instruccion_mdl.DoesNotExist:
		return redirect('comandos')

	if request.method == "POST":
		contenidoForm = frm_comandos_items(comandoId,request.POST,request.FILES,instance=datos)
		if contenidoForm.is_valid():
			contenidoForm.save()
			return redirect('comandos')

	

	formulario = frm_comandos_items(comandoId,instance = datos )
	contexto = {'formulario':formulario ,'mensaje':'Editar instruccion  '}
	return render(request,'comandos_modificar_itemComando.html',contexto)




@login_required
def view_comando_simple(request,id_comando):
	usuario = User.objects.select_related().get(id=request.user.id)
	try: 
		comando = mdl_comandos.objects.select_related().filter(usuario=usuario).get(id=id_comando)

		intrucciones = instruccion_mdl.objects.filter(comando=comando)


	except mdl_comandos.DoesNotExist:
		return redirect('inicio')

	contexto = {"comando":comando,"intrucciones":intrucciones}		
	return render(request,"comandos_detalles.html",contexto)

def view_comando_simple_publico(request,id_comando):
	try: 
		comando = mdl_comandos.objects.select_related().filter(estado=True).get(id=id_comando)
		intrucciones = instruccion_mdl.objects.filter(comando=comando)		
	except mdl_comandos.DoesNotExist:
		return redirect('inicio')
	contexto = {"comando":comando,"intrucciones":intrucciones}		
	return render(request,"comandos_detalles_publico.html",contexto)


@login_required
def view_eliminar_comando(request,id_comando):
	usuario = User.objects.select_related().get(id=request.user.id)
	comando = mdl_comandos.objects.select_related().filter(usuario=usuario).get(id=id_comando)
	comando.delete()
	return redirect("comandos")	


@login_required
def view_eliminar_comando_item(request,id_comando,id_comandoItem):
	try:
		comandoId = get_object_or_404(mdl_comandos, usuario=request.user.id,id=id_comando)
	except Http404:
		return redirect('comandos')

	try:
		comandoItem = instruccion_mdl.objects.select_related().filter(comando=comandoId).get(id=id_comandoItem)
	except instruccion_mdl.DoesNotExist:
		return redirect('comandos')

	comandoItem.delete()
	return redirect("comandos")	