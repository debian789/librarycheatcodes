from django.forms import ModelForm, Textarea
from apps.codigos.models import mdl_codigos
from apps.elementos_comunes.models import *
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django_ace import AceWidget


SIN_OPCION = [
('','Lenguaje de Progrmacion')
]

class frm_codigos(ModelForm):

	def __init__(self, *args, **kwargs):
		super(frm_codigos, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['titulo','links','lenguaje','archivo','descripcion','codigo','usuario','favorito']

	class Meta:
			model = mdl_codigos
			fields=(
					'titulo',
					'descripcion',
					'links',					
					'lenguaje',
					'archivo',
					'codigo',
					'estado',
				)
			widgets = {
			'titulo':forms.TextInput(attrs={'required':'','title':'Se necesita un Titulo'}),
			'lenguaje':forms.Select(attrs={'required':'','title':'Se necesita un Lenguaje '}),
			'codigo':AceWidget(mode='python',width="100%",height="500px",theme='twilight',attrs={'required':'','title':'Se necesita un Codigo '}),
			'links':forms.URLInput(attrs={'title':'http://pagina.com o http://www.pagina.com','pattern':"https?://.+"}),
			}

	def __init__(self, usuario, *args, **kwargs):
		super(frm_codigos, self).__init__(*args, **kwargs)
		self.usuario = usuario

 	def save(self, commit=True,*args,**kwargs):
		codigos_ingresados = super(frm_codigos, self).save(commit=False, *args, **kwargs)
		codigos_ingresados.usuario = self.usuario

		if commit: 
			codigos_ingresados.save()

		return codigos_ingresados

class frm_codigos_busqueda(forms.Form):

	busqueda = forms.CharField(required=False,label='',max_length = 200, widget=forms.TextInput(attrs={'class': 'input',
			   'placeholder':'Buscar'
			   },) )
	lenguaje = forms.CharField(required=False,label="Lenguaje de Programacion",max_length = 200 ,  widget=forms.Select(
		choices= SIN_OPCION + list(mdl_lenguaje.objects.all().values_list('id','nombre')),  ))
	adjunto = forms.BooleanField(required=False,label="Archivo Adjunto")
	#text = forms.CharField(widget=AceWidget(mode='python', theme='twilight'))
	