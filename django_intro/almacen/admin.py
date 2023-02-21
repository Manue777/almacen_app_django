from django.contrib import admin
from .models import ProductosModel, CategoriasModel, ClientesModel

# Register your models here.

class ShowFields(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'estado')

admin.site.register(ProductosModel, ShowFields)


class ShowFields(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'dni')
admin.site.register(ClientesModel, ShowFields)

class ShowFields(admin.ModelAdmin):
    list_display = ('nombre', 'estado')
admin.site.register(CategoriasModel, ShowFields)