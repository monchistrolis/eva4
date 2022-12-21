from django.db import models

# Create your models here.

class Libro(models.Model):

    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(auto_now_add=True)


class Autor(models.Model):

    nombre = models.CharField(max_length=100)



class Editorial(models.Model):

    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
