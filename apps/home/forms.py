from django import forms 

class loginForm(forms.Form):
	userName = forms.CharField(required=False,label='',max_length = 200, widget=forms.TextInput(attrs={'class': 'input',
			   'placeholder':'Username'
			   },) )
	password = forms.CharField(label='',widget=forms.PasswordInput(render_value=False,attrs={'class': 'input',
			   'placeholder':'Password'
			   }))