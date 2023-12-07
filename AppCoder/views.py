from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
# Create your views here.

def inicio_view(xx):
    return HttpResponse("<h3>Hola, buenas tardes(o noches)<h3/>")



def curso_view(xx):
    nombre = "Tobias"
    edad = 30
    apellido = "Barbero"

    diccionario = {"nombre" : nombre,
                   "edad" : edad,
                   "apellido" : apellido,}
    

    ruta = "C:/Users/Usuario/Documents/Programacion/Python1/Proyecto-Coder-Final/AppCoder/templates/AppCoder/Padre.html"

    
    archivo = open(ruta, 'r')
    
    plantilla = Template(archivo.read())
    contexto = Context(diccionario)
    documento = plantilla.render(contexto)

    return HttpResponse(documento)
    