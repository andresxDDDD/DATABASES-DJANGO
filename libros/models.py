from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    autor = models.CharField(max_length=150, verbose_name="Autor")
    # Usamos IntegerField para el año, ya que solo necesitamos el número de cuatro dígitos
    anio_publicacion = models.IntegerField(verbose_name="Año de publicación")
    # Un campo booleano que por defecto estará en True (disponible)
    disponible = models.BooleanField(default=True, verbose_name="¿Está disponible?")

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


