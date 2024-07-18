from django import forms
from .models import Cliente, Contacto
from django.forms import ModelForm
from .models import Genero
from .models import Articulo
from .models import TipoProducto
from .models import Proveedor
from .models import Articulo


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_empresa', 'rut', 'razon_social', 'pais', 'tipo_pago']


class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['nombre', 'marca', 'procedencia', 'codigo']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['sku', 'nombre', 'descripcion', 'precio', 'stock']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut_cli', 'nombres', 'apellidos', 'email', 'direccion', 'telefono', 'comuna', 'region']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['correo', 'nombre_completo', 'telefono', 'consulta']
        labels = {
            'correo': 'Correo',
            'nombre_completo': 'Nombre Completo',
            'telefono': 'Teléfono',
            'consulta': 'Consulta',
        }

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ["genero",]
        labels = {'genero': 'Género', }

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['sku', 'nombre', 'descripcion', 'precio', 'stock']