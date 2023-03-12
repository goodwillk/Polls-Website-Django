from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return self.pub_date >= now - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
class SuggestQuestion(models.Model):
    firstName = models.CharField(max_length=100, blank=True, null= True)
    lastName = models.CharField(max_length=100)
    question = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return f"{self.question} --- By {self.firstName}"