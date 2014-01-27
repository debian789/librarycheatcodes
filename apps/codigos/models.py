#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from apps.elementos_comunes.models import *

class mdl_codigos(models.Model):
	titulo 		= models.CharField(max_length=500)
	descripcion = models.TextField(blank=True)
	links    	= models.URLField(max_length=300,blank=True)
	lenguaje    = models.ForeignKey(mdl_lenguaje,blank=False)
	archivo     = models.FileField(upload_to='archivoCodigos/',null=True,blank=True)
	codigo 		= models.TextField()
	usuario     = models.ForeignKey(User)
	favorito    = models.BooleanField(default=False,blank=False)
	fechaIngreso = models.DateField(auto_now = True)

	class Meta:
		verbose_name = ('Codigo')
		verbose_name_plural = ('Codigos')

	def __unicode__(self):
		return self.titulo

