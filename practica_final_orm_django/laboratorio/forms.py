from django.forms import *
from .models import Laboratorio

class LaboratorioForm(ModelForm):
    
    class Meta:
        model = Laboratorio
        fields = '__all__'
        labels = {
            'nombre':'Nombre del Laboratorio',
            'ciudad':'Ciudad',
            'pais':'País',
        }
        widgets = {
            'nombre':TextInput(
                attrs={
                    'class':'form-control mb-3'
                }
            ),
            'ciudad':TextInput(
                attrs={
                    'class':'form-control mb-3'
                }
            ),
            'pais':TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
        }
