from school.models import User, VirtualClass, Question, Exam

from school.serializers import (
    UserSerializer,
    VirtualClassSerializer,
    QuestionSerializer,
    ExamSerializer,
)

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VirtualClassListCreate(generics.ListCreateAPIView):
    queryset = VirtualClass.objects.all()
    serializer_class = VirtualClassSerializer


class VirtualClassRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VirtualClass.objects.all()
    serializer_class = VirtualClassSerializer


class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ExamListCreate(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamCorrection(APIView):
    def post(self, request, pk):
        try:
            exam = Exam.objects.get(pk=pk)
        except Exam.DoesNotExist:
            return Response(
                {"error": "Este exame não foi encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if exam.is_done:
            return Response(
                {"error": "Esta prova já foi corrigida"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if "answers" not in request.data:
            return Response(
                {"error": "O campo de 'answers' é obrigatório"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user_answers = request.data.get("answers", [])
        correct_answers = 0
        wrong_answers = []

        for answer in user_answers:
            question_id = answer.get("question_id")
            user_answer = answer.get("user_answer")
            question = Question.objects.get(pk=question_id)

            if question.answer == user_answer:
                correct_answers += 1
            else:
                wrong_answers.append(
                    {
                        "question_id": question_id,
                        "user_answer": user_answer,
                        "correct_answer": question.answer,
                    }
                )

        exam.is_done = True
        exam.score = correct_answers
        exam.save()

        exam.user_answers = {
            "correct_answers": correct_answers,
            "wrong_answers": wrong_answers,
        }

        return Response(
            {
                "correct_answers": correct_answers,
                "wrong_answers": wrong_answers,
            },
            status=status.HTTP_200_OK,
        )
