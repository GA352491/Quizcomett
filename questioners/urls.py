from django.contrib import admin
from django.urls import path
from questioners.views import QuestionAPI

urlpatterns = [
    path('questions/', QuestionAPI.as_view()),
]
