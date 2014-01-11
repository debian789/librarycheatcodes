from apps.codigos.models import *
from django.contrib.auth.models import User 

class mdl_favoritos(models.Model):
	codigo = models.ForeignKey(mdl_codigos)
	tiempo_registro = models.DateTimeField(auto_now=True)