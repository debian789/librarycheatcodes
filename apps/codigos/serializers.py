from rest_framework import serializers
from apps.codigos.models import mdl_codigos
from apps.elementos_comunes.models import mdl_lenguaje, mdl_sistema_operativo

class codigosSerializer(serializers.HyperlinkedModelSerializer ):					   
	class Meta:
		model = mdl_codigos
		fields = ("url","titulo","descripcion","url","so","lenguaje","archivo","codigo","publicado")


class lenguajeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = mdl_lenguaje
		fields = ("nombre",)

class soSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = mdl_sistema_operativo
		fields = ('nombre',)



