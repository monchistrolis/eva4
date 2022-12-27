from django.contrib import admin
from .models import Autor, Libro, Editor

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha_publicacion','autores')
   

class EditorAdmin(admin.ModelAdmin):
    list_display = ('nombre','ubicacion','libros')


# Register your models here.
