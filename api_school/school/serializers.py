from school.models import User, VirtualClass, Question, Exam
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(required=False)
    extra_kwargs = {"password": {"write_only": True}}
    virtual_class = serializers.PrimaryKeyRelatedField(
        queryset=VirtualClass.objects.all(), required=False
    )

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("As duas senhas não são iguais.")
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            cpf=validated_data["cpf"],
            name=validated_data["name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
        )
        if "is_staff" in validated_data and validated_data["is_staff"]:
            user.is_staff = validated_data["is_staff"]
        if validated_data["is_student"] and validated_data["is_teacher"]:
            raise serializers.ValidationError(
                "Um Usuário não pode ser aluno e professor ao mesmo tempo."
            )
        if not validated_data["is_student"] and not validated_data["is_teacher"]:
            raise serializers.ValidationError(
                "Um usuário deve obrigatoriamente ser aluno ou professor."
            )
        if validated_data["is_student"]:
            user.is_student = validated_data["is_student"]
            if "virtual_class" in validated_data:
                user.virtual_class = validated_data["virtual_class"]
            else:
                raise serializers.ValidationError(
                    "Um estudante deve possuir uma turma associada"
                )
        if validated_data["is_teacher"]:
            if "virtual_class" in validated_data:
                raise serializers.ValidationError(
                    "Não deve-se informar o campo de virtual_class para um professor."
                )
            user.is_teacher = validated_data["is_teacher"]
        user.save()
        return user


class VirtualClassSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = VirtualClass
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.get("teacher")

        virtual_class = VirtualClass(
            grade=validated_data["grade"], letter=validated_data["letter"]
        )

        if not user.is_teacher:
            raise serializers.ValidationError("O usuário não é professor")

        virtual_class.teacher = user
        virtual_class.save()

        return virtual_class


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False)
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )

    class Meta:
        model = Exam
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.get("user")
        if user.is_teacher:
            raise serializers.ValidationError(
                "Um professor não pode responder uma prova"
            )
        exam = Exam.objects.create(**validated_data)

        questions = Question.objects.all().order_by("?")[:5]

        exam.questions.set(questions)

        exam.save()
        return exam
