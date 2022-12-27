from django.contrib import admin
from django.urls import path

# importar vistas
from .views import crear_libro,listar_libros,modificar_libro,eliminar_libro

urlpatterns = [
    path('crear_libro/', crear_libro),
    path('listar_libros/', listar_libros),
    path('modificar_libro/<int:pk>', modificar_libro),
    path('eliminar_libro/<int:pk>', eliminar_libro),
]