from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body','answer')
#Quiz 모델 데이터가 주어지면 title, body, answer를 
#포함한 JSON 데이터로 변환해주는 시리얼라이저

