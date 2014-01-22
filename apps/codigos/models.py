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

	# def upload_to(instance, filename):
	# 	model = instance._meta.module_name
	# 	MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT')
	# 	new_filename = slugify('.'.join(filename.split('.')[:-1]))+'.'+filename.split('.')[-1].lower()
	# 	path = '%s/uploads/%s/%s/' % (MEDIA_ROOT, model, instance.id)
	# 	if not os.path.exists('%s/uploads/%s/' % (MEDIA_ROOT, model), 0755):
	# 		if not os.path.exists(path):
	# 			os.mkdir(path,0755)
	# 		return 'uploads/%s/%s/%s' % (model, instance.id, new_filename)
	# 	else:
	# 		if not os.path.exists('%s/uploads/%s/new/' % (MEDIA_ROOT, model)):
	# 			os.mkdir('%s/uploads/%s/new/' % (MEDIA_ROOT, model), 0755)
	# 		return 'uploads/%s/new/%s' % (model, new_filename)


	#def imagen_azul_publicado(self):
	#	return 'http://placehold.it/200x100/28137F/13f5ff/&text=%d+votos' % self.publicado

	#def esta_publicado(self):
	#	return self.publicado == True

	#esta_publicado.boolean = True

#class Agregador(models.Model):
#    titulo = models.CharField(max_length=140)
#    enlaces = models.ManyToManyField(mdl_codigos) 


# Create your models here.
