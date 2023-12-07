from school.models import User, VirtualClass, Question, Exam, Result

from school.serializers import (
    UserSerializer,
    VirtualClassSerializer,
    QuestionSerializer,
    ExamSerializer,
    ResultSerializer,
)

from rest_framework import generics


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


class ResultListCreate(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
