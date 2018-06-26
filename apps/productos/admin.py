from django.contrib import admin

from django.contrib import admin
from .models import *
from apps.almacen.models import *
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    model=Categoria

@admin.register(Producto)
class ProductosAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('codigo','descripcion','categoria','stock_minimo',)
    list_editable = ('descripcion','categoria','stock_minimo',)

@admin.register(ProductoMedida)
class ProductoMedidaAdmin(admin.ModelAdmin):
    model = ProductoMedida
    list_display = ('codigo_producto','id_unidad','valor',)
    list_editable = ('id_unidad','valor',)

@admin.register(UnidadMedicion)
class UnidadMedicionAdmin(admin.ModelAdmin):
    model = UnidadMedicion
    def __str__(self):
        return 'Unidades de Medida'

@admin.register(GuiaRemision)
class GuiaDeRemisionAdmin(admin.ModelAdmin):
    model = GuiaRemision
    list_display = ('id','fecha_ingreso','nro_guia_remitente','proveedor')
    list_editable = ('fecha_ingreso','nro_guia_remitente','proveedor')

