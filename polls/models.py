import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    @admin.display(
        boolean=True,
        # ordering='pub_date',
        description='Published recently?',
    )
    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def total_votes(self):
        choices = self.choice_set.all()
        votes_list = map(lambda choice: choice.votes, choices)
        return sum(votes_list)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    votes = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
