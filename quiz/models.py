from django.db import models

# Create your models here.
#퀴즈모델 생성
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
