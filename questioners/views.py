from django.shortcuts import render
from rest_framework.views import APIView, Response
from drf_yasg.utils import swagger_auto_schema
from accounts.models import CustomUser
from questioners.models import Question
from questioners.serializers import QuestionSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class QuestionAPI(APIView):
    @swagger_auto_schema(responses={200: QuestionSerializer(many=True)})
    def get(self, request):
        questions = Question.objects.all()
        question_serializer = QuestionSerializer(questions, many=True)
        return Response({'data': question_serializer.data})
