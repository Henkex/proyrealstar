from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=15)
    def __str__(self):
        return  self.nombre

class UnidadMedicion(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True, max_length=10)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.ForeignKey(Categoria,blank=True,null=True, on_delete=models.CASCADE)
    stock_minimo = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.descripcion


class ProductoMedida(models.Model):
    id_unidad = models.ForeignKey(UnidadMedicion,blank=True,null=True, on_delete=models.CASCADE)
    codigo_producto = models.ForeignKey(Producto,blank=True,null=True, on_delete=models.CASCADE)
    valor = models.DecimalField('Valor S/.',max_digits=4,decimal_places=2)

    class Meta:
        unique_together = (("id_unidad", "codigo_producto"),)

