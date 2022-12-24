from django.db import models

# Create your models here.class Libro(models.Model):
class Autor(models.Model):
    nombre = models.CharField(max_length=255)

    
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    autores = models.ManyToManyField(Autor)

class Editor(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    libros = models.ManyToManyField(Libro)


