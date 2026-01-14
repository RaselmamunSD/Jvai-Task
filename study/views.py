from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import PermissionDenied

from .models import Flashcard, Quiz, MatchingItem, Note
# Create your views here.
from .serializers import (
    UserRegisterSerializer,
    FlashcardSerializer,
    QuizSerializer,
    MatchingItemSerializer,
    NoteSerializer,
)

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """
    Simple registration endpoint.

    POST /api/auth/register/
    {
      "username": "rasel",
      "email": "rasel@gmail.com",
      "password": "123456"
    }
    """

    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer


class OwnerQuerySetMixin:
    

    def get_queryset(self):
        # Only return objects belonging to the current user
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Set the owner to the current user when creating new objects
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.owner != self.request.user:
            # Extra safety check (should not normally happen because of get_queryset)
            raise PermissionDenied("You do not have permission to edit this item.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You do not have permission to delete this item.")
        instance.delete()


class FlashcardViewSet(OwnerQuerySetMixin, viewsets.ModelViewSet):
    
    serializer_class = FlashcardSerializer
    queryset = Flashcard.objects.all()


class QuizViewSet(OwnerQuerySetMixin, viewsets.ModelViewSet):
    
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class MatchingItemViewSet(OwnerQuerySetMixin, viewsets.ModelViewSet):
    

    serializer_class = MatchingItemSerializer
    queryset = MatchingItem.objects.all()


class NoteViewSet(OwnerQuerySetMixin, viewsets.ModelViewSet):
    
    # Full CRUD for notes.
    

    serializer_class = NoteSerializer
    queryset = Note.objects.all()
