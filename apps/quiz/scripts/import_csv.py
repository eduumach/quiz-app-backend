import csv

from apps.quiz.models import Quiz, IncorrectAnswer, Category, Difficulty, Type


def import_csv():
    with open('quiz.csv', 'r') as (file):
        reader = csv.reader(file)
        for row in reader:
            print(row)
            quiz = Quiz()
            quiz.difficulty = Difficulty.objects.get_or_create(name=row[0])[0]
            quiz.type = Type.objects.get_or_create(name=row[1])[0]
            quiz.category = Category.objects.get_or_create(name=row[2])[0]
            quiz.question = row[3]
            quiz.correct_answer = row[4]
            quiz.save()
            for i in range(5, 8):
                if row[i] != '':
                    IncorrectAnswer.objects.create(quiz=quiz, incorrect_answer=row[i])


import_csv()
