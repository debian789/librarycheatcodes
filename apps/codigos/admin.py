from django.contrib import admin
from models import mdl_codigos
from apps.elementos_comunes.models  import mdl_lenguaje,mdl_sistema_operativo
from actions import export_as_csv

## crea el listado de opciones en el administrado !!! 
class codigosAdmin(admin.ModelAdmin):
	list_display  = ('titulo','lenguaje','archivo','imagen_azul','esta_publicado','url')
	list_filter   = ('publicado','so','lenguaje')
	search_fields = ('titulo','codigo')
	list_editable = ('archivo',)
	actions       = [export_as_csv] 
	raw_id_fields = ('lenguaje',)
	filter_horizontal = ('so',)

	def imagen_azul(self,obj):
		url = obj.imagen_azul_publicado()
		tag = '<img src="%s">'% url 
		return tag
	imagen_azul.allow_tags = True  #permite que tenga tag html
	imagen_azul.admin_order_field = 'publicado' #permite ordenarlos por publicado


class CodigosInline(admin.StackedInline):
	model = mdl_codigos
	extra = 1

class LenguajesAdmin(admin.ModelAdmin):
	actions = [export_as_csv]
	inlines = [CodigosInline]


#class SitemaOperativoAdmin(admin.ModelAdmin):
#	fiter_vertical = ('so',)
#class AgregadorAdmin(admin.ModelAdmin):
#	filter_vertical = ('enlaces',)

admin.site.register(mdl_sistema_operativo)
#admin.site.register(Agregador,AgregadorAdmin)
#admin.site.register(mdl_sistema_operativo)
#admin.site.register(mdl_lenguaje,LenguajesAdmin)
admin.site.register(mdl_lenguaje)

admin.site.register(mdl_codigos,codigosAdmin)
#admin.site.register(soAdmin)
#admin.site.register(mdl_lenguaje,LenguajesAdmin)