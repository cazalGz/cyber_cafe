from django.shortcuts import render, redirect
from django.contrib.auth import logout
from Menu.models import Producto
from comentarios.models import Comentario
from nosotros.models import Galeria
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def crear_comentario(request):
    if request.method == 'POST':
        texto = request.POST['texto'].strip()
        if texto:
            comentario = Comentario(usuario=request.user, texto=texto)
            comentario.save()
        else:
            messages.error(request, "El comentario no puede estar vacío.")
    return redirect('inicio')
    



def inicio(request):
    productos = Producto.objects.all()
    comentarios = Comentario.objects.all()
    galeria=Galeria.objects.all()
    return render(request, "inicio.html", {"productos": productos, "comentarios": comentarios, "galeria":galeria})

def exit(request):
    logout(request)
    return redirect('inicio')
