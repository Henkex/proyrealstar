from django.contrib import admin
from django import forms
from .models import Empresa
from app.general import mensaje_aplicacion


class FormRucValidator(forms.ModelForm):
	class Meta:
		model = Empresa
		exclude = ()
	
	def clean_ruc(self):
		ruc=self.cleaned_data.get("ruc")
		if len(str(ruc)) > 9:
			raise forms.ValidationError(mensaje_aplicacion.RUC_INVALID)
		elif len(str(ruc)) < 8:
			raise forms.ValidationError(mensaje_aplicacion.RUC_INVALID)
		return ruc


#Esto se mostrará en la lista principal 
class EmpresaAdmin(admin.ModelAdmin):
	form = FormRucValidator
	list_display = ('ruc','rz','direc','logo')

admin.site.register(Empresa,EmpresaAdmin)
