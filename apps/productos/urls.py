from django.conf.urls import url
from .views import *
app_name='productos'
urlpatterns = [
 	url(r'^$', Index.as_view(),name='index'),
    url(r'^listar$', ListarProductos.as_view(),name='Listar_Productos'),
    url(r'^stock$', ListarStock.as_view(),name='Listar_stock'),
    url(r'^eliminar/(?P<pk>\d+)/$', EliminarProducto.as_view(),name='Eliminar_Producto'),
    #url(r'^registrar$',RegistrarProducto.as_view(),name='Registrar_Producto'),
    #url(r'^editar/(?P<pk>\d+)/$',EditarProducto.as_view(),name='Editar_Producto'),
    url(r'^registrar$',RegistrarProducto.as_view(),name='Registrar_Producto'),
    url(r'^editar/(?P<pk>\d+)',Editar_Producto.as_view(),name='Editar_Producto'),
    url(r'^categoria$',Categorias.as_view(),name='Categorias'),
    url(r'editar_categoria/(\d+)/$',Editar_Categoria,name='Editar_Categoria'),
    url(r'^eliminar_categoria/(?P<pk>\d+)/$', EliminarCategoria.as_view(),name='Eliminar_Categoria')
]