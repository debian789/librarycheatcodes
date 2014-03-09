from django.forms import ModelForm, Textarea 

from django import forms
from models import *
from django_ace import AceWidget

class frm_comandos(ModelForm):

	def __init__(self,*args,**kwargs):
		super(frm_comandos,self).__init__(*args,**kwargs)
		self.fields.keyOrder = ["nombre","descripcion","comando"]


	class Meta:
			model = mdl_comandos
			fields = (
				"nombre",
				"descripcion",
				"comando"
				)

			widgets = {
			'nombre':forms.TextInput(attrs={'required':'','title':'Se necesita un Nombre'}),
			'descripcion':forms.Textarea(attrs={'required':'','title':'Se necesita una Descripcion '}),
			'comando':AceWidget(mode='python',width="100%",theme='twilight',attrs={'required':'','title':'Se necesita un Comando  '}),
			}

	def __init__(self, usuario, *args, **kwargs):
		super(frm_comandos, self).__init__(*args, **kwargs)
		self.usuario = usuario

	def save(self, commit=True,*args,**kwargs):
		comando_ingresado = super(frm_comandos, self).save(commit=False, *args, **kwargs)
		comando_ingresado.usuario = self.usuario

		if commit: 
			comando_ingresado.save()

		return comando_ingresado


class frm_comandos_busqueda(forms.Form):

	busqueda = forms.CharField(required=False,label='',max_length = 200, widget=forms.TextInput(attrs={'class': 'input',
			   'placeholder':'Buscar'
			   },) )