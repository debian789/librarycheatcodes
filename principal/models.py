from codigos.models import *
from django.contrib.auth.models import User 


TIPO_FAVORITO =  (
	('codigo','codigo'),
	('proyecto','proyecto')
	)


class mdl_favoritos(models.Model):
	codigo = models.ForeignKey(mdl_codigos)	
	#place = models.OneToOneField(Place, primary_key=True)
	#codigo          = models.
	#tipo            = models.charField(choice=TIPO_FAVORITO)
	#tiempo_registro = models.DateTimeField(auto_now=True)

class mdl_mensajes(models.Model):
	mensaje 		 = models.CharField(max_length=500)