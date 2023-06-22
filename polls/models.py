from django.db import models

from django.contrib import admin

import datetime

from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published") #auto_now_add=True
    
    def __str__(self):
    	return self.question_text
    #decorador 	para ejecutar (modifica comportamento) antes de was_published_recently
    @admin.display(boolean=True,ordering="pub_date",description="Published recently?",)
    def was_published_recently(self):
    	now = timezone.now()
    	return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.boolean = True


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    #si se deja da error con votes de Votes
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)   
    votes = models.IntegerField(default=0)
    vote_date = models.DateTimeField("date vote")
    ip = models.CharField(max_length=20)

    def __str__(self):
        return str(self.choice) + ": " + str(self.votes)