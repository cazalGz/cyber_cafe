from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from Menu.models import Producto, Categoria



class MenuView(ListView):
    model = Producto
    template_name = 'menu/menu.html'
    context_object_name = 'productos'
    paginate_by = 12  # Mostrar 12 productos por página

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class MenuPorCategoriaView(ListView):
    template_name = 'menu/menu_categoria.html'
    context_object_name = 'productos'
    paginate_by = 12

    def get_queryset(self):
        categoria_slug = self.kwargs['categoria_slug']
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        return Producto.objects.filter(categoria=categoria)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_slug = self.kwargs['categoria_slug']
        context['categoria_actual'] = get_object_or_404(Categoria, slug=categoria_slug)
        return context
