#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from apps.elementos_comunes.models import *

class mdl_proyectos(models.Model):
	nombre 		 = models.CharField(max_length=500,verbose_name="Nombre")
	descripcion  = models.TextField(verbose_name="Descripción",blank=True)
	version 	 = models.CharField(max_length=100,verbose_name="Version",blank=True,null=True)
	link 		 = models.URLField(max_length=300,verbose_name="Url",blank=True,null=True)
	lenguaje    = models.ForeignKey(mdl_lenguaje,blank=False)
	Nivel		 = models.ForeignKey(mdl_nivel_desarrollo,verbose_name="Nivel de Desarrollo")
	os 			 = models.ForeignKey(mdl_sistema_operativo,verbose_name="Sistema Operativo")
	interfaz	 = models.ForeignKey(mdl_interfaz_aplicacion,verbose_name="Interfaz de Aplicación")
	usuario     = models.ForeignKey(User)
	archivo 	 = models.FileField(upload_to='archivoProyectos',null=True,blank=True,verbose_name="Archivo Adjunto")
	favorito    = models.BooleanField(default=False,blank=False)
	fechaIngreso = models.DateField(auto_now = True)
	estado       = models.BooleanField(default = False)
	

	class Meta:
		verbose_name = ('Proyecto')
		verbose_name_plural = ('Proyectos')

	def __unicode__(self):
		return self.nombre
