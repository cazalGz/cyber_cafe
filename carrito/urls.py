from django.urls import path
from . import views

urlpatterns = [
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('hacer_compra/', views.hacer_compra, name='hacer_compra'),
    
]
