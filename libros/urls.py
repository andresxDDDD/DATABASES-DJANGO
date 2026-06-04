from django.urls import path
from . import views  # Importamos el archivo views.py completo

urlpatterns = [
    path("", views.listar_libros, name="listar_libros"),
]