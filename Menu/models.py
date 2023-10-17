from django.db import models
from django.utils.text import slugify
# Create your models here.

class Categoria(models.Model):
    categoria=models.CharField(max_length=30)
    slug = models.SlugField(unique=True, default='valor-predeterminado')  # Agregar un campo slug

    def save(self, *args, **kwargs):
        # Generar automáticamente el slug a partir del nombre de la categoría
        self.slug = slugify(self.categoria)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.categoria

class Producto(models.Model):
    nombre=models.CharField(max_length=30)
    descripción=models.CharField(max_length=200)
    precio=models.FloatField()
    imagen=models.ImageField(upload_to='Menu')
    creado=models.DateTimeField(auto_now_add=True)
    modificado=models.DateTimeField(auto_now_add=True)
    categoria=models.ManyToManyField(Categoria)
    

    def __str__(self):
        return self.nombre


