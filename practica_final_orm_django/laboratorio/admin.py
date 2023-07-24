from django.contrib import admin
from .models import *

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'laboratorio']


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'f_fabricacion', 'p_costo', 'p_venta']
    list_filter = ['nombre', 'laboratorio']

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)