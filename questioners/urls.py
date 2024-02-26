from django.contrib import admin
from django.urls import path
from questioners.views import QuestionAPI,QuestionEachAPI

urlpatterns = [
    path('questions/', QuestionAPI.as_view()),
    path('question/', QuestionEachAPI.as_view()),
]
