from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz, Question, Option, PDFDocument
from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer
from .utils import extract_text_from_pdf
from .quiz_generator import generate_quiz

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_quiz(request):
    try:
        data = request.data
        serializer = QuizSerializer(data=data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': f'{e} Exception Occurred at server'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_quizzes(request):
    try:
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'{e} Exception Occurred at server'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_pdf_generate_quiz(request):
    try:
        pdf_file = request.FILES.get('pdf_file')
        title = request.data.get('title')

        if not pdf_file:
            return Response({'error': 'No PDF file provided.'}, status=status.HTTP_400_BAD_REQUEST)
        if not title:
            return Response({'error': 'No title provided.'}, status=status.HTTP_400_BAD_REQUEST)

        pdf_document = PDFDocument(user=request.user, title=title, pdf_file=pdf_file)
        pdf_document.save()

        pdf_path = pdf_document.pdf_file.path
        content = extract_text_from_pdf(pdf_path)

        quiz_data = generate_quiz(content)

        return Response({
            'message': 'PDF uploaded and quiz generated successfully.',
            'quiz_data': quiz_data
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': f'{e} Exception Occurred at server'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)