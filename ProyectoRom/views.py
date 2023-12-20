from django.http import HttpResponse 
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render, redirect
from ProyectoRom.forms import FormularioLogin, EjemploFormulario
from ProyectoRom.models import Usuario, Roms


def roms(xx):
  
    
    diccionario = {}
    
    
    plantilla = loader.get_template('Roms.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)
def emuladores(xx):
   
    
    diccionario = {}
    
    
    plantilla = loader.get_template('Emuladores.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)
def login(request):
   
    
    if request.method == "POST":
        miForm = FormularioLogin(request.POST)
        print (miForm)
        if miForm.is_valid():
            info = miForm.cleaned_data
            usuario =  Usuario(nombre = info["nombre"], email = info["email"], contra = info["contra"])
            usuario.save()
            return redirect( "home")
    else:   
        miForm = FormularioLogin()
        return render(request,"Login1.html", {"miForm":miForm})
            

def buscarRoms(request):
    return render(request, "buscarRoms.html")

def buscar(request):
    rom_id = request.GET.get('rom_id')

    if rom_id:
        rom = Roms.objects.filter(rom_id__icontains=rom_id)
        return render(request, "ProyectoRom/Plantilla/resultadosBusqueda.html", {"rom_id": rom_id, "rom": rom})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
    
    
    
    
def home(xx):
    
    
    diccionario = { }
    # html = open("C:/Users/Usuario/Documents/.programacion/Python1/ProyectoFinalRoms/ProyectoRom/ProyectoRom/Plantilla/template1.html")
    # plantilla = Template(html.read())
    
    # html.close()
    # contexto = Context(diccionario)
    plantilla = loader.get_template('Home.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)



def ejemploformulario(request):
    if request.method == "POST":
        miForm = EjemploFormulario(request.POST)
        print (miForm)
        if miForm.is_valid:
            info = miForm.cleaned_data
            usuario =  Usuario(nombre = info["nombre"], email = info["email"], contra = info["contraseña"])
            usuario.save()
            return render(request, "Home.html")
    else:
        miForm = EjemploFormulario()
        return render(request,"ejemploformulario.html", {"miForm":miForm})


