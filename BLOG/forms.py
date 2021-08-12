from django import forms
from django.db.models.base import Model
from .models import Producto, Salud, Motricidad, Rincon

class FormProducto(forms.ModelForm): 

    #campos del modelo
    class Meta:
        model = Producto
        fields = ('titulo', 'descripcion', 'imagen', 'link')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
            'descripcion': forms.TextInput(attrs={'class': 'pub_descripcion'}),
            'imagen': forms.TextInput(attrs={'class': 'pub_imagen'}),
            'link': forms.TextInput(attrs={'class': 'pub_link'}),
        }

class FormSalud(forms.ModelForm): 

    #campos del modelo
    class Meta:
        model = Salud
        fields = ('titulo', 'descripcion', 'imagen', 'link')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
            'descripcion': forms.TextInput(attrs={'class': 'pub_descripcion'}),
            'imagen': forms.TextInput(attrs={'class': 'pub_imagen'}),
            'link': forms.TextInput(attrs={'class': 'pub_link'}),
        }


class FormMotricidad(forms.ModelForm): 

    #campos del modelo
    class Meta:
        model = Motricidad
        fields = ('titulo', 'descripcion', 'imagen', 'link')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
            'descripcion': forms.TextInput(attrs={'class': 'pub_descripcion'}),
            'imagen': forms.TextInput(attrs={'class': 'pub_imagen'}),
            'link': forms.TextInput(attrs={'class': 'pub_link'}),
        }

class FormRincon(forms.ModelForm): 

    #campos del modelo
    class Meta:
        model = Rincon
        fields = ('titulo', 'descripcion', 'imagen', 'link')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
            'descripcion': forms.TextInput(attrs={'class': 'pub_descripcion'}),
            'imagen': forms.TextInput(attrs={'class': 'pub_imagen'}),
            'link': forms.TextInput(attrs={'class': 'pub_link'}),
        }