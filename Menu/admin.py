from django.contrib import admin
from .models import Producto, Categoria
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    readonly_fields=('creado','modificado')




admin.site.register(Producto, MenuAdmin)

admin.site.register(Categoria)