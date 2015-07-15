from django.contrib import admin
from models import mdl_comandos,comando_mdl



admin.site.register(mdl_comandos)


@admin.register(comando_mdl)
class comandoAdmin(admin.ModelAdmin):
	pass



