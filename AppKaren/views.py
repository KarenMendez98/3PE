from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *


def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal de Trotamundos")

def inicioApp(request):
    return render(request, "AppKaren/inicio.html")

def destinos(request):
    return render(request, "AppKaren/destinos.html")

def paquetes(request):
    return render(request, "AppKaren/paquetes.html")



def viajeros(request):
    
    if request.method =="POST":
        form = PasajeroForm(request.POST)
        if form.is_valid():
            viajero = Viajero()
            viajero.nombre= form.cleaned_data["nombre"]
            viajero.apellido = form.cleaned_data["apellido"]         
            viajero.email = form.cleaned_data["email"]
            viajero.destino= form.cleaned_data["destino"]
            viajero.save()
            form = PasajeroForm()
    else:
        form = PasajeroForm()

    viajeros = Viajero.objects.all()
    context ={"viajeros": viajeros, "form": form}       
    return render(request, "AppKaren/viajeros.html", context)



def paquetes(request):
    
    if request.method =="POST":
        form = PaqueteForm(request.POST)
        if form.is_valid():
            paquete = Paquete()
            paquete.lugar = form.cleaned_data["lugar"]
            paquete.cant_dias = form.cleaned_data["cant_dias"]         
            paquete.cant_pasajeros = form.cleaned_data["cant_pasajeros"]
            paquete.save()
            form = PaqueteForm()
    else:
        form = PaqueteForm()

    paquetes = Paquete.objects.all()
    context ={"paquetes": paquetes, "form": form}       
    return render(request, "AppKaren/paquetes.html", context)



def destinos(request):
    
    if request.method =="POST":
        form = VisitaGForm(request.POST)
        if form.is_valid():
            visita = Visita()
            visita.tipo = form.cleaned_data["tipo"]
            visita.ciudad = form.cleaned_data["ciudad"]         
            visita.save()
            form = VisitaGForm()
    else:
        form = VisitaGForm()

    visitas = Visita.objects.all()
    context ={"visitas": visitas, "form": form}       
    return render(request, "AppKaren/destinos.html", context)


def busquedaActividad(request):
    return render(request, "AppKaren/busquedaActividad.html")


def buscar(request):
    ciudad = request.GET["ciudad"]

    if ciudad!="":
        visitas= Visita.objects.filter(ciudad = ciudad)
        return render(request, "AppKaren/resultadosBusqueda.html", {"visitas": visitas, "ciudad": ciudad})
    
    else:
        return render(request, "AppKaren/busquedaActividad.html", {"mensaje": "Ingrese una ciudad válida"})