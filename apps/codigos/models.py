from django.db import models
from apps.elementos_comunes.models import *


def url(self,filename):
		ruta = "ArchivosAdjuntos/archivos/%s"% filename
		return ruta

class mdl_codigos(models.Model):
	titulo 		= models.CharField(max_length=500)
	descripcion = models.TextField()
	url    		= models.URLField(max_length=300)
	so 			= models.ManyToManyField(mdl_sistema_operativo) 
	lenguaje    = models.ForeignKey(mdl_lenguaje)
	archivo     = models.ImageField(upload_to=url,null=True,blank=True)
	codigo 		= models.TextField()
	publicado 	= models.BooleanField(default=True)	


	class Meta:
		verbose_name = ('Codigo')
		verbose_name_plural = ('Codigos')

	def __unicode__(self):
		return self.titulo

	def imagen_azul_publicado(self):
		return 'http://placehold.it/200x100/28137F/13f5ff/&text=%d+votos' % self.publicado

	def esta_publicado(self):
		return self.publicado == True

	esta_publicado.boolean = True

#class Agregador(models.Model):
#    titulo = models.CharField(max_length=140)
#    enlaces = models.ManyToManyField(mdl_codigos) 


# Create your models here.
