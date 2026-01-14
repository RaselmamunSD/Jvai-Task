from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class TimeStampedModel(models.Model):
    
    # Simple abstract base model to add created/updated timestamps.
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Flashcard(TimeStampedModel):
    
    #A basic flashcard with a front and back side.
    

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flashcards')
    front_text = models.CharField(max_length=255)
    back_text = models.TextField()

    def __str__(self) -> str:
        return f'Flashcard({self.front_text[:30]!r})'


class Quiz(TimeStampedModel):
    
   # A very simple quiz model.

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self) -> str:
        return f'Quiz({self.title!r})'


class MatchingItem(TimeStampedModel):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matching_items')
    left_text = models.CharField(max_length=255, help_text='For example: a word')
    right_text = models.CharField(max_length=255, help_text='For example: its meaning')

    def __str__(self) -> str:
        return f'MatchingItem({self.left_text!r} -> {self.right_text!r})'


class Note(TimeStampedModel):
    
    # study note.
    

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self) -> str:
        return f'Note({self.title!r})'
