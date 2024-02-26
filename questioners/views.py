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
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class QuestionAPI(APIView):
    @swagger_auto_schema(responses={200: QuestionSerializer(many=True)})
    def get(self, request):
        questions = Question.objects.all()
        question_serializer = QuestionSerializer(questions, many=True)
        return Response({'data': question_serializer.data})


from rest_framework import pagination


class MyPageNumberPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'limit'


class QuestionEachAPI(APIView, MyPageNumberPagination):
    page_size = 1
    serializer_class = QuestionSerializer

    def get(self, request, format=None):
        try:
            questions_objs = Question.objects.all()
            results = self.paginate_queryset(questions_objs, request, view=self)
            questionsserializer = self.serializer_class(results, many=True)
        except Exception as e:
            return Response(str(e))
        return self.get_paginated_response(questionsserializer.data)
