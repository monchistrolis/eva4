from rest_framework import routers
from .api import LibroViewSet, AutorViewSet, EditorViewSet

router = routers.DefaultRouter()
router.register('api/libros', LibroViewSet, 'libros')
router.register('api/autores', AutorViewSet, 'autores')
router.register('api/editores', EditorViewSet, 'editores')

urlpatterns = router.urls