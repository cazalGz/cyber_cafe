from django.db import models
from Menu.models import Producto
from django.contrib.auth.models import User

class ItemCarrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)


class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Asócialo al usuario que hizo la compra si estás utilizando autenticación de usuarios
    fecha = models.DateTimeField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return f"Compra #{self.id} - {self.usuario} - {self.fecha}"