from django import forms

class EjemploFormulario(forms.Form):
    
    usuario = forms.CharField()
    email = forms.EmailField
    contra =forms.CharField()
    
class FormularioLogin(forms.Form):
    
    usuario = forms.CharField()
    email = forms.EmailField
    contra =forms.CharField()
    
