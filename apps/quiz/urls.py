from django.urls import path, include
from rest_framework import routers
from .views import QuizListView, CategoryListView, DifficultyListView, TypeListView

app_name = 'quiz'

router = routers.DefaultRouter()

urlpatterns = [
    path('quiz', QuizListView.as_view(), name='quiz-list'),
    path('category', CategoryListView.as_view(), name='category-list'),
    path('difficulty', DifficultyListView.as_view(), name='difficulty-list'),
    path('type', TypeListView.as_view(), name='type-list'),
    path('', include(router.urls)),
]
