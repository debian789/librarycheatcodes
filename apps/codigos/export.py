from import_export import resources
from apps.codigos.models import mdl_codigos
from apps.elementos_comunes.models import *

from import_export.admin import ImportExportModelAdmin


class resource_codigos_admin(ImportExportModelAdmin):
    resource_class = mdl_codigos
    pass



# class resource_codigos(resources.ModelResource):
# 	class Meta:
# 		model= mdl_codigos
# 		fields = ('titulo')