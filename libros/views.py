from django.shortcuts import render
from .models import Libro
# Create your views here.

def listar_libros(request):
    libros=Libro.objects.all()


    return render(request, "index.html", {"libros": libros})
    pass