from django.contrib import admin 
from principal.models import GoogleAnalytics_mdl

@admin.register(GoogleAnalytics_mdl)
class GaleriaAdmin(admin.ModelAdmin):
	pass