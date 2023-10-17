from django.urls import path

from nosotros import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('nosotros/',views.nosotros, name="nosotros"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)