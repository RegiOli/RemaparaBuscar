from django import forms
from .models import RespuestaFormulario, RespuestaDestinoFinal

class RespuestaFormularioForm(forms.ModelForm):
    class Meta:
        model = RespuestaFormulario
        fields = '__all__'

class RespuestaDestinoFinalForm(forms.ModelForm):
    class Meta:
        model = RespuestaDestinoFinal
        fields = '__all__'
