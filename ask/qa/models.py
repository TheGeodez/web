from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length= 500)
    text = models.TextField()
    added_at = models.DateField(blank=True)
    rating = models.IntegerField()
    author = models.CharField(max_length=150)
    likes = models.ManyToManyField( User, related name = 'question_like_user')
    objects = QuestionManager()


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(blank=True)
    question = models.OneToOneField(Question)
    author = models.CharField(max_length=200)
