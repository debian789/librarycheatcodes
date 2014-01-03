#encoding:utf-8
from django.db import models
from apps.elementos_comunes.models import *

def url(self,filename):
	ruta = 'ArchivosProyectos/archivos/%s' % filename
	return ruta


class mdl_proyectos(models.Model):
	nombre 		 = models.CharField(max_length=500,verbose_name="Nombre")
	descripcion  = models.TextField(verbose_name="Descripción")
	version 	 = models.CharField(max_length=100,verbose_name="Version")
	url 		 = models.URLField(max_length=300,verbose_name="Url")
	Nivel		 = models.ForeignKey(mdl_nivel_desarrollo,verbose_name="Nivel de Desarrollo")
	os 			 = models.ForeignKey(mdl_sistema_operativo,verbose_name="Sistema Operativo")
	interfaz	 = models.ForeignKey(mdl_interfaz_aplicacion,verbose_name="Interfaz de Aplicación")
	archivo 	 = models.FileField(upload_to=url,null=True,blank=True,verbose_name="Archivo Adjunto")
	publicado 	 = models.BooleanField(default=True)
	fechaIngreso = models.DateField(auto_now = True)

	class Meta:
		verbose_name = ('Proyecto')
		verbose_name_plural = ('Proyectos')

	def __unicode__(self):
		return self.nombre


# Create your models here.
