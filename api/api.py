from api.models import Libro, Autor, Editor
from rest_framework import viewsets, permissions
from .serializers import LibroSerializer, AutorSerializer, EditorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AutorSerializer

class EditorViewSet(viewsets.ModelViewSet):
    queryset = Editor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EditorSerializer



