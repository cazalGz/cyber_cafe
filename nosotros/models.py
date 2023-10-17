from django.db import models

# Create your models here.

class Contacto(models.Model):
    instagram=models.URLField(blank=True, null=True)
    facebook=models.URLField(blank=True, null=True)
    whatsapp=models.URLField(blank=True, null=True)
    nrotelefono=models.CharField(blank=True, null=True, max_length=15)
    correo=models.EmailField(blank=True, null=True)
    def __str__(self):
        return 'instagram: %s. facebook: %s. whatsapp: %s. nrotelefono: %s. correo: %s.' %(self.instagram, self.facebook, self.whatsapp, self.nrotelefono, self.correo)

class Quienes_somos(models.Model):
    descripción=models.CharField(max_length=500)

class Galeria(models.Model):
    foto=models.ImageField(blank=True, null=True)






