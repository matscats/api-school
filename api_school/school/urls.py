from school.views import (
    UserListCreate,
    UserRetrieveUpdateDestroy,
    VirtualClassListCreate,
    VirtualClassRetrieveUpdateDestroy,
    QuestionListCreate,
    QuestionRetrieveUpdateDestroy,
    ExamListCreate,
    ExamRetrieveUpdateDestroy,
    ExamCorrection,
)
from django.urls import path

urlpatterns = [
    path("user/", UserListCreate.as_view()),
    path("user/<int:pk>/", UserRetrieveUpdateDestroy.as_view()),
    path("virtual_class/", VirtualClassListCreate.as_view()),
    path("virtual_class/<int:pk>/", VirtualClassRetrieveUpdateDestroy.as_view()),
    path("question/", QuestionListCreate.as_view()),
    path("question/<int:pk>/", QuestionRetrieveUpdateDestroy.as_view()),
    path("exam/", ExamListCreate.as_view()),
    path("exam/<int:pk>/", ExamRetrieveUpdateDestroy.as_view()),
    path("exam/<int:pk>/send/", ExamCorrection.as_view()),
]
