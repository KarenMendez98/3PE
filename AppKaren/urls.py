from django.urls import path
from .views import *


urlpatterns = [
    
    path("", inicioApp, name="inicioApp"),
    path("viajeros/", viajeros, name="viajeros"),
    path("destinos/", destinos, name="destinos"),
    path("paquetes/", paquetes, name="paquetes"),
]