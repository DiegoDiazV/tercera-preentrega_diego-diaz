from django import forms
from TerceraPreentregaApp.models import Categoria

class ClienteForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=50
    )
    nombre.widget.attrs.update({
        'class':'form-control'
    })
    apellido = forms.CharField(
        label="Apellido",
        max_length=50
    )
    apellido.widget.attrs.update({
        'class':'form-control'
    })
    telefono = forms.CharField(
        label="Teléfono",
        max_length=11
    )
    telefono.widget.attrs.update({
        'class':'form-control'
    })
    email = forms.CharField(
        label="Email",
        max_length=50
    )
    email.widget.attrs.update({
        'class':'form-control'
    })

class ProductoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=50
    )
    nombre.widget.attrs.update({
        'class':'form-control'
    })
    precio = forms.IntegerField(
        label="Precio"
    )
    precio.widget.attrs.update({
        'class':'form-control text-right'
    })
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    categoria.widget.attrs.update({
        'class':'form-control'
    })

class CategoriaForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=50
    )
    nombre.widget.attrs.update({
        'class':'form-control'
    })

class BusquedaForm(forms.Form):
    search_text = forms.CharField(
        label="Buscar",
        max_length=50
    )
    search_text.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Cliente o Producto'
    })
