from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length= 500)
    text = models.TextField()
    added_at = models.DateField(blank=True)
    rating = models.IntegerField()
    author = models.CharField(max_length=150)
    likes = models.TextField()
    QuestionManager = models.Manager()


class QuestionManager(models.Manager):
    def popular(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * 
            FROM Question
            ORDER BY rating""")



class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(blank=True)
    question = models.OneToOneField(Question)
    author = models.CharField(max_length=200)
