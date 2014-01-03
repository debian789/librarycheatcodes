from django.forms import ModelForm, Textarea
from apps.codigos.models import mdl_codigos
from apps.elementos_comunes.models import *
from django import forms

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class frm_codigos(ModelForm):
	def __init__(self, *args, **kwargs):
		super(frm_codigos, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['titulo','url','lenguaje','so','archivo','descripcion','codigo','publicado']

	class Meta:
			model = mdl_codigos


class frm_codigos_busqueda(forms.Form):
	buesqueda = forms.CharField(label='',max_length = 200, widget=forms.TextInput(attrs={'class': 'input',
			   'placeholder':'Buscar'
			   },) )
	#lenguaje = forms.CharField(max_length = 200 ,  widget=forms.Textarea())
	#lenguaje = forms.CharField(max_length = 200 ,  widget=forms.Select(choices=TITLE_CHOICES))
	lenguaje = forms.CharField(label="Lenguaje de Programacion",max_length = 200 ,  widget=forms.Select(
		
		choices=mdl_lenguaje.objects.all().values_list('id','nombre'),  ))

	sistema = forms.CharField(label="Sistema Operativo",max_length = 200 ,  widget=forms.Select(
		
		choices=mdl_sistema_operativo.objects.all().values_list('id','nombre')  ))
	adjunto = forms.BooleanField(label="Archivo Adjunto")

	