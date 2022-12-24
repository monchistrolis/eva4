from django import forms
from .models import Libro, Autor, Editor


#creacion de libros
class BookForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'fecha_publicacion', 'autores', 'editor')

#creacion de autores
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre',)

#creacion de editoriales
class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = ('nombre', 'ubicacion')


