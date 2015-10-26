from django.shortcuts import render_to_response,get_object_or_404,render,redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from codigos.models import *
from comandos.models import *
from proyectos.models import *
from principal.forms import RegistroPersonaForm
from models import *
from forms import *
#from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='inicio')
def view_inicio_sesion(request):
	usuario = User.objects.select_related().get(id=request.user.id)
	codigos = mdl_codigos.objects.select_related().filter(usuario=usuario)[:4]
	comandos = mdl_comandos.objects.select_related().filter(usuario=usuario)[:4]
	#proyectos = mdl_proyectos.objects.select_related().filter(usuario=usuario)[:4]
	# codigos = mdl_codigos.objects.select_related().filter(usuario=usuario)
	# favoritos = mdl_favoritos.objects.select_related().filter(codigo=codigos)
	# ultimoCodigo = mdl_codigos.objects.select_related().filter(usuario=usuario)[:10]
	#contexto = {"favoritos":favoritos,"codigos":ultimoCodigo}
	contexto = {"codigos":codigos,"comandos":comandos}# ,"proyectos":proyectos}
	return render(request,"inicioSesion.html",contexto)



# def view_inicio(request):
# 	return render(request,'index.html')

def view_salir(request):
	logout(request)
	return redirect('inicio')


def view_inicio(request):
	if request.user.is_authenticated():	
		return redirect('inicio_sesion')
	else:
		codigos = mdl_codigos.objects.select_related().filter(estado=True)[:4]
		comandos = mdl_comandos.objects.select_related().filter(estado=True)[:4]
		proyectos = mdl_proyectos.objects.select_related().filter(estado=True)[:4]
		contexto = {"codigos":codigos,"comandos":comandos,"proyectos":proyectos}
		return render(request,"inicio.html",contexto)	



def view_ingresar(request):
	mensaje=""
	if request.user.is_authenticated():
		return redirect('inicio_sesion')
		#return HttpResponseRedirect('/inicioSesion')

	else:
		if request.method == "POST":
			form = loginForm(request.POST)
			if form.is_valid():
				username= form.cleaned_data['userName']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return redirect('inicio_sesion')
					#return HttpResponseRedirect('/inicioSesion')

				else:
					mensaje = "Usuario o Password incorrectos "

		form = loginForm()
		contexto = {'form':form,'mensaje':mensaje}
		# print mensaje
		return render(request,'login.html',contexto)




def registrarPersonaView(request):
	if request.method == 'POST':
		formulario = RegistroPersonaForm(request.POST)
		if formulario.is_valid():
			formulario.save()

			usuario = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password2'])

			if usuario is not None:
				login(request,usuario)

				return redirect('inicio_sesion')

	else:
		formulario = RegistroPersonaForm()

	contexto = {'form':formulario}
	return render(request,'registro-persona.html', contexto)






# def view_agregar_favoritos(request,id_codigo):
# 	usuario   = User.objects.select_related().get(id=request.user.id)
# 	codigo    = mdl_codigos.objects.get(id=id_codigo,usuario=usuario)
# 	datosTemp = mdl_favoritos.objects.create(codigo=codigo)
# 	datosTemp.save()
# 	codigo.favorito = True 
# 	codigo.save()

# 	codigos = mdl_codigos.objects.all()
# 	contexto = {"codigos":codigos}
# 	return render(request,'codigos.html',contexto)

# @login_required
# def view_quitar_favorito(request,id_codigo):
# 	codigo = mdl_codigos.objects.get(id=id_codigo)
# 	datos = mdl_favoritos.objects.filter(codigo=codigo).delete()
# 	#datos.save()
# 	codigo.favorito = False
# 	codigo.save()

# 	codigos = mdl_codigos.objects.all()
# 	contexto = {"codigos":codigos}
# 	return render(request,'codigos.html',contexto)

# @login_required
# def view_quitar_favorito_principal(request,id_codigo):
# 	codigo = mdl_codigos.objects.get(id=id_codigo)
# 	datos = mdl_favoritos.objects.filter(codigo=codigo).delete()
# 	codigo.favorito = False
# 	codigo.save()
# 	usuario = User.objects.select_related().get(id=request.user.id)
# 	codigos = mdl_codigos.objects.select_related().filter(usuario=usuario)
# 	favoritos = mdl_favoritos.objects.select_related().filter(codigo=codigos)
# 	ultimoCodigo = mdl_codigos.objects.select_related().filter(usuario=usuario)[:10]
# 	#codigos = mdl_codigos.objects.all()[:2]
# 	#codigo
# 	contexto = {"favoritos":favoritos,"codigos":ultimoCodigo}
# 	return render(request,"inicioSesion.html",contexto)

# @login_required
# def view_agregar_proyecto_favoritos(request,id_proyecto):
# 	usuario   = User.objects.select_related().get(id=request.user.id)
# 	proyecto  = mdl_proyectos.objects.get(id=id_proyecto,usuario=usuario)

