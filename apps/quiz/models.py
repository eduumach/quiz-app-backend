from django.db import models


class Quiz(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    difficulty = models.ForeignKey('Difficulty', on_delete=models.CASCADE)
    question = models.TextField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Quizzes'


class IncorrectAnswer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='incorrect_answers')
    incorrect_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.incorrect_answer

    class Meta:
        verbose_name_plural = 'Incorrect Answers'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Difficulty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Difficulties'


class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Types'
