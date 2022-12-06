from django import forms
from .models import *

class DateInput(forms.DateTimeInput):
    input_type = 'date'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = ['id_prof','nombre','apellido','rut','email','telefono','fecha','hora','diab','coment',]
        labels ={
            'id_prof':'Atencion',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'rut':'Rut',
            'email':'Correo (email)',
            'telefono':'Telefono',
            'fecha':'Fecha',
            'hora':'Horario',
            'diab':'Es diabetico?',
            'coment':'Comentarios',
        }
        widgets = {
            'nombre':forms.TextInput({'class' : 'form-control'}),
            'diab':forms.Select({'class' : 'form-control'}),
            'rut':forms.TextInput({'class' : 'form-control'}),
            'id_prof':forms.Select({'class' : 'form-control'}),
            'apellido':forms.TextInput({'class' : 'form-control'}),
            'email':forms.EmailInput({'class' : 'form-control'}),
            'telefono':forms.TextInput({'class' : 'form-control'}),
            'fecha': DateInput(attrs={'class':'form-control'}),
            'hora':forms.Select({'class' : 'form-control'}),
            'coment':forms.Textarea({'class' : 'form-control'}),
        }

        



 
        
