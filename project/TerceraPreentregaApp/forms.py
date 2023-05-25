from django import forms

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
        max_length=9
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