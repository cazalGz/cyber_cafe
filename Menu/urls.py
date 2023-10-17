from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/categoria/<slug:categoria_slug>/', views.MenuPorCategoriaView.as_view(), name='menu_categoria'),

]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
