# from django.http import HttpResponse
# from django.template import Template, Context
# from django.template.loader import get_template
from django.shortcuts import render
import datetime
from django.http import HttpResponse

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):
    persona1 = Persona("Cristian", "Ramirez")
    fecha = datetime.datetime.now()
    ctx = {"nombre_persona":persona1.nombre, "apellido_persona":persona1.apellido, "ahora":fecha}
    return render(request, 'archivoHtml.html', ctx)

def hosting(request):
    fecha = datetime.datetime.now()
    return render(request, 'hosting.html', {"fecha":fecha})

def correo(request):
    fecha = datetime.datetime.now()
    return render(request, 'correo.html', {"fecha": fecha})

def buscar(request):
    msj= "El resulado de la busqueda es %r" %request.GET["productos"]
    return HttpResponse(msj)

