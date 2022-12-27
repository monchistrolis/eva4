from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,permission_classes)

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Libro, Autor, Editor
from .serializers import LibroSerializer, AutorSerializer, EditorSerializer

# Create your views here.
#creacion de libros
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def crear_libro(request):
    serializer = LibroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#listado de libros
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listar_libros(request):
    libros = Libro.objects.all()
    serializer = LibroSerializer(libros, many=True)
    return Response(serializer.data)

#modificacion de libros
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def modificar_libro(request, pk):
    libro = Libro.objects.get(id=pk)
    serializer = LibroSerializer(instance=libro, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#eliminacion de libros
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def eliminar_libro(request, pk):
    libro = Libro.objects.get(id=pk)
    libro.delete()
    return Response('Libro eliminado')

