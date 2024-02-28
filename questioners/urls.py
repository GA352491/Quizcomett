from django.contrib import admin
from django.urls import path
from questioners.views import QuestionAPI, QuestionEachAPI, CategoryAPI

urlpatterns = [
    path('questions/', QuestionAPI.as_view()),
    path('question/<category>', QuestionEachAPI.as_view()),
    path('categories/', CategoryAPI.as_view()),
]
