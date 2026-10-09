from django.urls import path, include
from rest_framework import routers

from api.views import TagViewSet, CategoryViewSet, NotesViewSet

router = routers.DefaultRouter()

router.register('tags', TagViewSet, basename='tags')
router.register('categories', CategoryViewSet, basename='categories')
router.register('notes', NotesViewSet, basename='notes')

urlpatterns = [
    path('', include(router.urls)),
]