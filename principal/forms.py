from django import forms 

from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class loginForm(forms.Form):
	userName = forms.CharField(required=False,label='',max_length = 200, widget=forms.TextInput(attrs={'class': 'input',
			   'placeholder':'Username'
			   },) )
	password = forms.CharField(label='',widget=forms.PasswordInput(render_value=False,attrs={'class': 'input',
			   'placeholder':'Password'
			   }))


class RegistroPersonaForm(UserCreationForm):
	""" Formulario de login de usuario """
	email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'input','required':''}))
	#first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'input','required':''}))
	#telefono = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'input','required':''}))
	#direccion = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'input','required':''}))
	username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'input','required':''}))
	#userName = forms.CharField(required=False,label='',max_length = 200, widget=forms.TextInput(attrs={'class': 'input',
	#		   'placeholder':'Username'
	#		   },) )
	password1 = forms.CharField(label='',widget=forms.PasswordInput(render_value=False,attrs={'class': 'input',
			   'placeholder':'Password','required':''
			   }))

	class Meta:
		model = User 
		fields = ("username","email", "password1", "password2")

	def save(self, commit=True):
		user = super(RegistroPersonaForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
		    user.save()
		    