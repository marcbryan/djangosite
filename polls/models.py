from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

class Vote(models.Model):
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
