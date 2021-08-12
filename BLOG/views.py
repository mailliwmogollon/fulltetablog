from django.shortcuts import render
from .forms import *
from .models import Producto, Salud, Motricidad, Rincon
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, "fullteta/index.html")

def lactancia(request):
    return render(request, "fullteta/lactancia.html", {
        "lista_principal": Producto.objects.all()
    })

def salud(request):
    return render(request, "fullteta/salud.html", {
        "lista_salud": Salud.objects.all()
    })

def motricidad(request):
    return render(request, "fullteta/motricidad.html", {
        "lista_motricidad": Motricidad.objects.all()
    })

def rincon(request):
    return render(request, "fullteta/rincon.html", {
        "lista_rincon": Rincon.objects.all()
    })

def busqueda(request):
   q = request.GET.get('q', '')

   querys = (Q(titulo__icontains=q) | Q(descripcion__icontains=q))

   producto = Producto.objects.all().filter(querys)
   salud1 = Salud.objects.all().filter(querys)
   motricidad1 = Motricidad.objects.all().filter(querys)
   rincon1 = Rincon.objects.all().filter(querys)

   return render(request, "fullteta/busqueda.html", {
        "producto": producto,
        "salud1": salud1,
        "motricidad1": motricidad1,
        "rincon1": rincon1,
       })