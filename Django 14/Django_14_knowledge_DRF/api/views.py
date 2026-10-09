from rest_framework import viewsets
from api.serializers import TagSerializer, CategorySerializer, NoteSerializer
from notes.models import Note, Tag, Category

from api.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.db.models import Q


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.select_related('author', 'category').prefetch_related('tags')
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_authenticated:
            return queryset.filter(status='published')
        return queryset.filter(Q(author=self.request.user) | Q(status='published'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
