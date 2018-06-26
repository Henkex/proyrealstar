from django import forms
from django.forms import ModelForm, formset_factory, inlineformset_factory
from .models import Producto,Categoria,UnidadMedicion,ProductoMedida
from apps.general import mensaje_aplicacion


class ProductoForm(forms.ModelForm):
    descripcion = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción'}),
                                  label="Descripcion")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
                                       widget=forms.Select(attrs={'class':'form-control','placeholder':'Categoría'}),
                                       label="Categoria",empty_label="Seleccione una categoria")
    stock_minimo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',
                                                                      'placeholder':'Stock mínimo'}),
                                      label="Stock Minimo")
    def clean_stock(self):
        stock_minimo = self.cleaned_data.get("stock_minimo")
        if stock_minimo < 0:
            raise forms.ValidationError(mensaje_aplicacion.STOCK_MUST_BE_POSITIVE)
        return stock_minimo
    class Meta:
        model = Producto
        fields = ('descripcion','categoria','stock_minimo',)

class UnidadProductoForm(forms.ModelForm):
    id_unidad = forms.ModelChoiceField(queryset=UnidadMedicion.objects.all(),
                                       widget=forms.Select(attrs={'class':'form-control'}),
                                       label="Valor",
                                       empty_label='Seleccione una unidad de medida')
    valor = forms.DecimalField(max_digits=4,decimal_places=2,
                                      widget=forms.NumberInput(attrs={'class':'form-control',
                                                                      'placeholder':'Valor S/.'}),
                                      label="Valor")
    def clean_valor(self):
        valor = self.cleaned_data.get("valor")
        if valor < 0:
            raise forms.ValidationError(mensaje_aplicacion.VALOR_MUST_BE_POSITIVE)
        return valor
    class Meta:
        model = ProductoMedida
        fields = ['id_unidad','valor',]

UnidadProductoFormSet = inlineformset_factory(Producto,ProductoMedida,UnidadProductoForm, extra=1, max_num=2,)
UnidadProductoFormSetEdit = inlineformset_factory(Producto,ProductoMedida,UnidadProductoForm, extra=0, max_num=2,min_num=1,can_delete=True)

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nueva categoria','required':True}),label="Nombre")
    class Meta:
        model = Categoria
        fields = ['nombre',]