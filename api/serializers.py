from rest_framework import serializers
from .models import Libro, Autor, Editor

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('titulo', 'fecha_publicacion', 'autores', 'editor')

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('nombre',)

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = ('nombre', 'ubicacion')

