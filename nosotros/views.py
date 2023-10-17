from django.shortcuts import render
from nosotros.models import Contacto, Quienes_somos, Galeria
import Templates

def nosotros(request):
    nosotros=Quienes_somos.objects.all()
    contacto=Contacto.objects.all()
    galeria=Galeria.objects.all()
    return render(request, "nosotros/nosotros.html", {"nosotros": nosotros, "contacto": contacto, "galeria":galeria})




