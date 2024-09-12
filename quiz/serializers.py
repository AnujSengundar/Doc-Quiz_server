from rest_framework import serializers
from .models import Quiz, Question, Option, PDFDocument

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'options']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_by', 'created_at', 'questions']
        read_only_fields = ['created_by', 'created_at']

class PDFDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDocument
        fields = ['id', 'user', 'title', 'pdf_file', 'uploaded_at']
        read_only_fields = ['uploaded_at', 'user']
