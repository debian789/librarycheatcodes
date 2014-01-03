from django.db import models



class mdl_sistema_operativo(models.Model):
	nombre = models.CharField(max_length= 200)

	class Meta:
		verbose_name = ('Sistema Operativo')
		verbose_name_plural = ('Sistema Operativos')

	def __unicode__(self):
		return self.nombre


class mdl_lenguaje(models.Model):
	nombre = models.CharField(max_length = 300)

	class Meta:
		verbose_name = ('Lenguaje')
		verbose_name_plural = ('Lenguajes')

	def __unicode__(self):
		return self.nombre

class mdl_interfaz_aplicacion(models.Model):
	nombre = models.CharField(max_length = 300)

	class Meta:
		verbose_name = ('Interfaz de aplicacion')
		verbose_name_plural = ('Interfaz de aplicaciones')

	def __unicode__(self):
		return self.nombre


class mdl_nivel_desarrollo(models.Model):
	nombre = models.CharField(max_length= 200)

	class Meta:
		verbose_name = ('Nivel de desarrollo')
		verbose_name_plural = ('Nivel de desarrollos')

	def __unicode__(self):
		return self.nombre


#class nueva(models.Model):
#	so = models.ForeignKey(mdl_sistema_operativo)
#	nombre = models.CharField(max_length=100)


# Create your models here.
