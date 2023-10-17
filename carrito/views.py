from django.shortcuts import render, redirect
from .models import Producto, ItemCarrito, Compra
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def ver_carrito(request):
    items = ItemCarrito.objects.all()
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'carrito/carrito.html', {'items': items, 'total': total})


@login_required
def agregar_al_carrito(request, producto_id):
    if not request.user.is_authenticated:
        # Si el usuario no está autenticado, mostrar un mensaje y redirigir a la página de inicio de sesión
        messages.error(request, 'Debes iniciar sesión para hacer la compra.')
        return redirect('login/')
    
    productos_en_carrito = ItemCarrito.objects.filter(usuario=request.user)
    if productos_en_carrito.count() >= 3:
        messages.error(request, 'No puedes agregar más de 3 productos al carrito.')
        return redirect('menu')

    producto = Producto.objects.get(id=producto_id)

    # Verificar si el producto ya está en el carrito
    item, creado = ItemCarrito.objects.get_or_create(usuario=request.user, producto=producto)

    if not creado:
        if item.cantidad >= 3:
            messages.error(request, 'No puedes agregar más de 3 unidades de este producto al carrito.')
        else:
            item.cantidad += 1
            item.save()

    return redirect('ver_carrito')

def eliminar_del_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    try:
        item = ItemCarrito.objects.get(producto=producto)
        item.delete()
    except ItemCarrito.DoesNotExist:
        pass
    return redirect('ver_carrito')

@login_required
def hacer_compra(request):
    if not request.user.is_authenticated:
        # Si el usuario no está autenticado, mostrar un mensaje y redirigir a la página de inicio de sesión
        messages.error(request, 'Debes iniciar sesión para hacer la compra.')
        return redirect('login/')  
    # Obtener el carrito del usuario
    items = ItemCarrito.objects.filter(usuario=request.user)

    if not items.exists():
        messages.error(request, 'Tu carrito está vacío. Agrega productos antes de hacer la compra.')
        return redirect('ver_carrito')
    # Crear una instancia de Compra
    compra = Compra(usuario=request.user)

    # Calcular el monto total de la compra
    monto_total = sum(item.producto.precio * item.cantidad for item in items)
    compra.monto_total = monto_total
    compra.save()

    # Asociar los productos comprados con la compra
    for item in items:
        compra.productos.add(item.producto)

    # Limpiar el carrito después de la compra
    items.delete()

    
    return render(request, 'carrito/confirmar_compra.html', {'compra': compra})


