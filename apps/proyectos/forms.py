from django.forms import ModelForm, Textarea 
from apps.elementos_comunes.models import *

from django import forms
from models import *

SIN_OPCION = {
	'lenguaje':[ ('','Lenguaje de Progrmacion')],
	'Nivel':[ ('','Nivel de Desarrollo ')],
	'os':[ ('','Sistema Operativo ')],
	'interfaz':[ ('','Interfaz de Aplicacion')],
}

class frm_proyectos(ModelForm):

	def __init__(self,*args,**kwargs):
		super(frm_proyectos,self).__init__(*args,**kwargs)
		self.fields.keyOrder = ["nombre","link","version","lenguaje","Nivel","os","interfaz","archivo","descripcion"]


	class Meta:
			model = mdl_proyectos
			fields = (
				"nombre",
				"link",
				"version",
				"lenguaje",
				"Nivel",
				"os",
				"interfaz",
				"archivo",
				"descripcion",
				"estado",
				)

			widgets = {
			'nombre':forms.TextInput(attrs={'required':'','title':'Se necesita un Nombre'}),
			'lenguaje':forms.Select(attrs={'required':'','title':'Se necesita un Lenguaje '}),
			'Nivel':forms.Select(attrs={'required':'','title':'Se necesita un Nivel de Desarrollo '}),
			'os':forms.Select(attrs={'required':'','title':'Se necesita un Sistema Operativo  '}),
			'interfaz':forms.Select(attrs={'required':'','title':'Se necesita una Intefaz '}),
			'link':forms.URLInput(attrs={'title':'http://pagina.com o http://www.pagina.com','pattern':"https?://.+"}),

			}

	def __init__(self, usuario, *args, **kwargs):
		super(frm_proyectos, self).__init__(*args, **kwargs)
		self.usuario = usuario

	def save(self, commit=True,*args,**kwargs):
		proyecto_ingresado = super(frm_proyectos, self).save(commit=False, *args, **kwargs)
		proyecto_ingresado.usuario = self.usuario

		if commit: 
			proyecto_ingresado.save()

		return proyecto_ingresado


class frm_proyectos_busqueda(forms.Form):

	busqueda = forms.CharField(required=False,label='',max_length = 200, widget=forms.TextInput(attrs={'class': 'input',
			   'placeholder':'Buscar'
			   },) )
	lenguaje = forms.CharField(required=False,label="Lenguaje de Programacion",max_length = 200 ,  widget=forms.Select(
		choices= SIN_OPCION["lenguaje"] + list(mdl_lenguaje.objects.all().values_list('id','nombre')),  ))

	Nivel = forms.CharField(required=False,label="Nivel de desarrollo ",max_length = 200 ,  widget=forms.Select(
		choices= SIN_OPCION["Nivel"] + list(mdl_nivel_desarrollo.objects.all().values_list('id','nombre')),  ))
	os = forms.CharField(required=False,label="Sistema operativo",max_length = 200 ,  widget=forms.Select(
		choices= SIN_OPCION["os"] + list(mdl_sistema_operativo.objects.all().values_list('id','nombre')),  ))
	interfaz = forms.CharField(required=False,label="Interfaz de aplicacion",max_length = 200 ,  widget=forms.Select(
		choices= SIN_OPCION["interfaz"] + list(mdl_interfaz_aplicacion.objects.all().values_list('id','nombre')),  ))

	#favorito = forms.BooleanField(label="Favorito")
	adjunto = forms.BooleanField(required=False,label="Archivo Adjunto")
