from rest_framework import serializers

from apps.quiz.models import Quiz, Category, Difficulty, Type


class QuizQuestionSerializer(serializers.ModelSerializer):
    incorrect_answers = serializers.ListSerializer(child=serializers.CharField(source='incorrect_answer'))

    class Meta:
        model = Quiz
        fields = ['category', 'type', 'difficulty',
                  'question', 'correct_answer', 'incorrect_answers']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
