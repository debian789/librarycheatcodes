from django.forms import ModelForm
from models import *


class frm_proyectos(ModelForm):
	class Meta:
			model = mdl_proyectos


