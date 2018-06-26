from django.forms.models import inlineformset_factory, formset_factory
from django import forms
from .models import GuiaRemision,Ingreso,DetalleIngreso,Proveedor,Salida,DetalleSalida,Almacen
from django.utils import timezone
from apps.productos.models import Producto,UnidadMedicion
from apps.usuarios.forms import User
from .models import Almacen

class UsuarioForm(forms.ModelForm):
    dni = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),
                                 label="Dni")
    class Meta:
        model=User
        fields = ('dni',)

class IngresoForm(forms.ModelForm):
    almacen = forms.ModelChoiceField(queryset=Almacen.objects.all(),
                                     widget=forms.Select(attrs={'class':'form-control ',
                                                                'placeholder':'almacen','required':True
                                                                }),empty_label="Escoga el almacén",
                                     label= 'Almacen')

    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(),
                                     widget=forms.Select(attrs={'class':'form-control ',
                                                                'placeholder':'proveedor','required':True
                                                                }),empty_label="Escoga el Proveedor",
                                     label= 'Proveedor')
    class Meta:
        model = Ingreso
        fields = ('tipo','dni_usuario','almacen','proveedor')


class DetalleIngresoForm(forms.ModelForm):
    # serie = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Serie'}),
    #                         label="Serie")
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',
                                                                  'placeholder':'Cantidad',
                                                                  'required':True}),
                                  label="Cantidad")
    unidad_caja = forms.ModelChoiceField(queryset=UnidadMedicion.objects.all(),
                                         widget=forms.Select(attrs={'class':'form-control ',
                                                                    'required':True,
                                                                    'placeholder':'Unidad de medida'}),
                                         empty_label="Escoja la unidad de medida")
    estado = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                           'placeholder':'Estado',
                                                           'required':True}),
                                                    label="Estado del producto")
    codigo_producto = forms.ModelChoiceField(queryset=Producto.objects.all(),empty_label="Escoja un producto",
                                            widget=forms.Select(attrs={'class':'form-control chosen-select',
                                                                     'placeholder':'Codigo',
                                                                     'required':True}))
    class Meta:
        model = DetalleIngreso
        fields = ('cantidad','unidad_caja','estado','codigo_producto',)

DetalleIngresoFormSet = inlineformset_factory(Ingreso,DetalleIngreso,extra=1,can_delete=False, form=DetalleIngresoForm)

class ProductoForm(forms.ModelForm):
    codigo_product = forms.ModelChoiceField(queryset=Producto.objects.all(),empty_label="Producto",
                                            widget=forms.Select(attrs={'class':'form-control',
                                                                       'required':True}),
                                            label="Codigo de producto")
    class Meta:
        model = Producto
        fields = ('codigo',)

class GuiaRemisionForm(forms.ModelForm):
    fecha_ingreso = forms.DateField(initial=timezone.now().strftime('%Y-%m-%d'),
                                     widget= forms.DateInput(attrs={'class':'form-control',
                                                                    'type':'date',
                                                                    'required':True}),
                                     label="Fecha de traslado")
    
    nro_guia_remitente = forms.CharField(max_length=11,
                                         widget=forms.TextInput(attrs={'class':'form-control',
                                                                       'placeholder':'Nro guia remitente',
                                                                       'required':True}),
                                         label="Guia remitente")
    class Meta:
        model= GuiaRemision
        fields = ('fecha_ingreso','nro_guia_remitente')


class ProveedoresForm(forms.ModelForm):
    ruc = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="RUC")
    nombre = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre")
    direccion = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="Direccion")

    class Meta:
        model = Proveedor
        fields = ('ruc','nombre','direccion',)

DetalleIngresoFormSet = inlineformset_factory(Ingreso,DetalleIngreso,
                                              can_delete=False,
                                              extra=2,
                                             max_num=3,
                                              form=DetalleIngresoForm)

#SALIDAS

class SalidaForm(forms.ModelForm):
    dni_usuario = forms.ModelChoiceField(queryset=User.objects.all(),
                                         widget=forms.Select(attrs={'class':'form-control','required':'true'}),
                                         empty_label="Escoja un usuario",
                                         label="Solicitante")
    nodo = forms.CharField(max_length=15,
                           widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el padron de Bus a trabajar'}),
                           label="Padron de Bus ",required=False)
    id_proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(),
                            widget=forms.Select(attrs={'class':'form-control ','placeholder':'proveedor','disabled':False}),
                            empty_label="Escoga el Proveedor si hay una devolucion",
                            label= 'Proveedor',required=False)
    devolucion = forms.BooleanField(initial=False,widget=forms.CheckboxInput(),
                                    label="Devolver productos defectuosos al proveedor",
                                    required=False)
    class Meta:
        model = Salida
        fields = ('dni_usuario','nodo','devolucion','id_proveedor')

class DetalleSalidaForm(forms.ModelForm):
    id_almacen = forms.ModelChoiceField(queryset=Almacen.objects.all(),
                                        widget=forms.Select(attrs={'class':'form-control c-almacen',
                                                                   'required':'true',}),
                                        label="Almacen",empty_label="Escoja un almacén")
    
    codigo_producto = forms.ModelChoiceField(Producto.objects,empty_label="Escoja un Producto",
                                             widget=forms.Select(attrs={'class':'form-control c-producto',
                                                                        'disabled': 'true'}))
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','disabled': 'true',
                                                                  'placeholder':'Unidades','min':'0'}),label="Cantidad")
    class Meta:
        model = DetalleSalida
        fields = ('codigo_producto','cantidad','id_almacen')

DetalleSalidaFormset = inlineformset_factory(Salida,DetalleSalida,extra=1,can_delete=True,form=DetalleSalidaForm)