from django.contrib import admin
from models import mdl_comandos,instruccion_mdl



admin.site.register(mdl_comandos)


@admin.register(instruccion_mdl)
class comandoAdmin(admin.ModelAdmin):
	pass



