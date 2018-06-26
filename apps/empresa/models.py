from django.db import models

# Create your models here.
class Empresa(models.Model):
	ruc=models.IntegerField(unique=True)
	rz=models.CharField(max_length=50, unique=True,verbose_name='Razón Social')
	direc=models.CharField(max_length=50, verbose_name='Dirección')
	logo=models.ImageField(upload_to='media/')	

	def __str__(self):
		return str(self.rz)