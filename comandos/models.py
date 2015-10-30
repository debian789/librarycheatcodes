#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from elementos_comunes.models import *

class mdl_comandos(models.Model):
	nombre       = models.CharField(max_length=500,verbose_name="Nombre")
	usuario      = models.ForeignKey(User)
	favorito     = models.BooleanField(default=False,blank=False)
	fechaIngreso = models.DateField(auto_now = True)
	estado       = models.BooleanField(default = False)
	
	def __unicode__(self):
		return self.nombre



class instruccion_mdl(models.Model):
	comando      = models.ForeignKey(mdl_comandos)
	instruccion      = models.CharField(max_length=500,verbose_name="Comando",blank=False,null=False)
	descripcion  = models.TextField(verbose_name="Descripción",blank=True)

	def __unicode__(self):
		return self.instruccion
