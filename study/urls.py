from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views


router = DefaultRouter()
router.register(r'flashcards', views.FlashcardViewSet, basename='flashcard')
router.register(r'quizzes', views.QuizViewSet, basename='quiz')
router.register(r'matching-items', views.MatchingItemViewSet, basename='matching-item')
router.register(r'notes', views.NoteViewSet, basename='note')

urlpatterns = [
    # Auth endpoints
    path('auth/register/', views.RegisterView.as_view(), name='auth-register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    # CRUD endpoints
    path('', include(router.urls)),
]


