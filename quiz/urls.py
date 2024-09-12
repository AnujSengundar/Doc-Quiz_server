# quiz/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # path('create/', create_quiz, name='create_quiz'),
    # path('list/', list_quizzes, name='list_quizzes'),
    path('upload-pdf/', upload_pdf_generate_quiz, name='upload_pdf_generate_quiz'),
]
