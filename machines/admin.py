from django.contrib import admin
from .models import Machines, Bitacora

# admin.site.register(Machines)
class MachinesAdmin(admin.ModelAdmin):
  list_display = ['nombre', 'codigo', 'marca', 'modelo', 'noSerie', 'equipo', 'area', 'responsable']
  list_filter =  ['area']
  search_fields = ['codigo', 'marca', 'modelo', 'noSerie', 'equipo', 'area', 'responsable', 'comentarios', 'manual']

admin.site.register(Machines, MachinesAdmin)

class BitacoraAdmin(admin.ModelAdmin):
  list_display = ['usuario', 'maquina', 'fecha', 'accion', 'tiempo_accion']
  list_filter =  ['fecha', 'maquina']
  search_fields = ['usuario', 'maquina', 'fecha', 'accion', 'tiempo_accion']

admin.site.register(Bitacora, BitacoraAdmin)