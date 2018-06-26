from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from apps.usuarios.views import Login,Logout
from django.conf.urls.static import static
from django.contrib.auth.views import login

urlpatterns = [
   path('admin/', admin.site.urls),
   path('login/', Login.as_view()),
   path('logout/', Logout.as_view()),
   path('',include('apps.almacen.urls', namespace='almacen')),
   url(r'^usuarios/',include('apps.usuarios.urls',namespace='usuarios')),
   url(r'^productos/',include('apps.productos.urls',namespace='productos')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
admin.site.site_header = 'Administrador BACKEND Real Star'
admin.site.site_title= "Interface web del administrador"