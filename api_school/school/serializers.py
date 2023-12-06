from school.models import User, VirtualClass, Question, Exam, Result
from rest_framework import serializers
import random


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(required=False)
    extra_kwargs = {"password": {"write_only": True}}

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("As duas senhas não são iguais.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            cpf=validated_data["cpf"],
            name=validated_data["name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
        )
        if "is_staff" in validated_data and validated_data["is_staff"]:
            user.is_staff = validated_data["is_staff"]
        if "is_student" in validated_data and validated_data["is_student"]:
            user.is_student = validated_data["is_student"]
        if "is_teacher" in validated_data and validated_data["is_teacher"]:
            user.is_teacher = validated_data["is_teacher"]

        return user


class VirtualClassSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = VirtualClass
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.get("user")

        virtual_class = VirtualClass.objects.create(
            grade=validated_data["grade"], letter=validated_data["letter"]
        )

        if user and user.is_teacher:
            virtual_class.teacher = user
            virtual_class.save()

        return virtual_class


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = "__all__"

    def create(self, validated_data):
        all_questions = Question.objects.all()
        random.shuffle(all_questions)
        selected_questions = all_questions[:10]
        exam = Exam.objects.create()
        exam.questions.set(selected_questions)

        return exam


class ResultSerializer(serializers.ModelSerializer):
    exam = ExamSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Result
        fields = "__all__"
