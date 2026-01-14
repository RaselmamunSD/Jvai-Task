from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Flashcard, Quiz, MatchingItem, Note

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Very small serializer for user registration.
    We explicitly write the `create` method to hash the password.
    """

    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'email': {'required': False},
        }

    def create(self, validated_data):
        # create_user handles password hashing and other details
        return User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email', ''),
            password=validated_data.get('password'),
        )


class FlashcardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Flashcard
        fields = ('id', 'owner', 'front_text', 'back_text', 'created_at', 'updated_at')


class QuizSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Quiz
        fields = ('id', 'owner', 'title', 'question', 'answer', 'created_at', 'updated_at')


class MatchingItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MatchingItem
        fields = ('id', 'owner', 'left_text', 'right_text', 'created_at', 'updated_at')


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ('id', 'owner', 'title', 'content', 'created_at', 'updated_at')


