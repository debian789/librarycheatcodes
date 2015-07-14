from django.contrib import admin
from models import mdl_codigos
from elementos_comunes.models  import mdl_lenguaje,mdl_sistema_operativo
from actions import export_as_csv

## crea el listado de opciones en el administrado !!! 
class codigosAdmin(admin.ModelAdmin):
	list_display  = ('titulo','lenguaje','archivo','links')
	list_filter   = ('lenguaje',)
	search_fields = ('titulo','codigo')
	list_editable = ('archivo',)
	actions       = [export_as_csv] 
	raw_id_fields = ('lenguaje',)

class CodigosInline(admin.StackedInline):
	model = mdl_codigos
	extra = 1

class LenguajesAdmin(admin.ModelAdmin):
	actions = [export_as_csv]
	inlines = [CodigosInline]

admin.site.register(mdl_sistema_operativo)
admin.site.register(mdl_lenguaje)
admin.site.register(mdl_codigos,codigosAdmin)
