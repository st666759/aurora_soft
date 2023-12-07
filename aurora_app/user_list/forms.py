from django import forms
from . models import user 


class userForm(forms.ModelForm):
    class Meta:
        model = user 
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name' : 'nombre',
            'apellido' : 'apellido', 
            'telefono' : 'telefono',
            'correo' : 'correo',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder' : 'ingresa el nombre'}),
            'apellido' : forms.TextInput(attrs={'placeholder' : 'ingresa tu apellido'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'ingresa tu númeor de telefono'}),
            'correo' : forms.TextInput(attrs={'placeholder' : 'ingresa tu correo electrónico'})
        }
