from django_filters.rest_framework import DjangoFilterBackend

from .models import Quiz, Category, Difficulty, Type
from rest_framework import generics
from .serializers import QuizQuestionSerializer, CategorySerializer, DifficultySerializer, TypeSerializer
import django_filters
from rest_framework.response import Response


class QuizFilter(django_filters.FilterSet):
    amount = django_filters.NumberFilter(method='filter_by_amount')

    def filter_by_amount(self, queryset, name, value):
        if value is not None:
            return queryset[:value]
        return queryset

    class Meta:
        model = Quiz
        fields = ['category', 'difficulty', 'type']


class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.order_by('?').all()
    serializer_class = QuizQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = QuizFilter


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DifficultyListView(generics.ListAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class TypeListView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
