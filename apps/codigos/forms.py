from django.forms import ModelForm, Textarea
from apps.codigos.models import mdl_codigos
from apps.elementos_comunes.models import *
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

SIN_OPCION = [
('','----')
]

class frm_codigos(ModelForm):

	def __init__(self, *args, **kwargs):
		super(frm_codigos, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['titulo','url','lenguaje','archivo','descripcion','codigo','usuario','favorito']
		self.fields['titulo'].widget.attrs.update({'class':'titulo'})


	class Meta:
			model = mdl_codigos
			fields=(
					'titulo',
					'descripcion',
					'url',					
					'lenguaje',
					'archivo',
					'codigo',
				)

	def __init__(self, usuario, *args, **kwargs):
		super(frm_codigos, self).__init__(*args, **kwargs)
		self.usuario = usuario

 	def save(self, commit=True,*args,**kwargs):
		codigos_ingresados = super(frm_codigos, self).save(commit=False, *args, **kwargs)
		codigos_ingresados.usuario = self.usuario

		if commit: 
			codigos_ingresados.save()

		return codigos_ingresados

	#so = forms.ModelMultipleChoiceField(queryset=mdl_codigos.objects.all(), widget=FilteredSelectMultiple("so",is_stacked=False))
	 # 	so = forms.ModelMultipleChoiceField(queryset=mdl_codigos.objects.all(),required=False,widget=FilteredSelectMultiple(('tags'),False,))

		# class Media:
		# 	css = {
		#     	'all':['admin/css/widgets.css',
		#           'css/uid-manage-form.css'],
		# 		}	# Adding this javascrip	t is crucial
		# 	js = ['/admin/jsi18n/']

        
	# def clean_titulo(self):
	# 	titulo_codigo = self.cleaned_data['titulo']
	# 	if not titulo_codigo:
	# 		raise forms.ValidationError('Este Campo es Obligatorio')

	# 	try: 
	# 		mdl_codigos.objects.filter(usuario=self.usuario).get(titulo=titulo_codigo)
	# 	except mdl_codigos.DoesNotExist:
	# 		return titulo_codigo
	# 	raise forms.ValidationError('Esta comunidad ya existe')











class frm_codigos_busqueda(forms.Form):

	busqueda = forms.CharField(required=False,label='',max_length = 200, widget=forms.TextInput(attrs={'class': 'input',
			   'placeholder':'Buscar'
			   },) )
	lenguaje = forms.CharField(required=False,label="Lenguaje de Programacion",max_length = 200 ,  widget=forms.Select(
		choices= SIN_OPCION + list(mdl_lenguaje.objects.all().values_list('id','nombre')),  ))
	#favorito = forms.BooleanField(label="Favorito")
	adjunto = forms.BooleanField(required=False,label="Archivo Adjunto")

	#lenguaje = forms.CharField(max_length = 200 ,  widget=forms.Select(choices=TITLE_CHOICES))
	#lenguaje = forms.CharField(max_length = 200 ,  widget=forms.Textarea())
	#sistema = forms.CharField(label="Sistema Operativo",max_length = 200 ,  widget=forms.Select(
	#	choices=mdl_sistema_operativo.objects.all().values_list('id','nombre')  ))
		

		

	