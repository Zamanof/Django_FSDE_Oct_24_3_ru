from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import TagSerializer, CategorySerializer, NoteSerializer, RegisterSerializer, LoginSerializer
from notes.models import Note, Tag, Category

from api.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

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


@method_decorator(csrf_protect, name='dispatch')
class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response({
            'id': user.id,
            'username': user.username,
            'message': 'Registration successful!'
        }, status=status.HTTP_201_CREATED)


# @method_decorator(csrf_protect, name='dispatch')
# class LoginView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         user = authenticate(
#             request,
#             username=serializer.validated_data['username'],
#             password=serializer.validated_data['password']
#         )
#         if user is None:
#             return Response({
#                 'error': 'Invalid username or password.'
#             }, status=status.HTTP_401_UNAUTHORIZED)
#
#         login(request, user)
#         return Response({
#             'message': 'Login successful!',
#             'username': user.username,
#         })
#
# class LogoutView(APIView):
#     authentication_classes = [SessionAuthentication]
