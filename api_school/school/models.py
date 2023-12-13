from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("O campo Email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        return self.create_user(email, password, **kwargs)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False, null=False, blank=False)
    is_teacher = models.BooleanField(default=False, null=False, blank=False)
    virtual_class = models.ForeignKey(
        "VirtualClass", null=True, on_delete=models.CASCADE, blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome", "sobrenome", "cpf"]

    def __str__(self):
        return f"{self.name} {self.last_name}"


class VirtualClass(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    grade = models.PositiveSmallIntegerField()
    letter = models.CharField(max_length=1)

    def __str__(self) -> str:
        return f"{self.grade}º {self.letter}"


class Question(models.Model):
    subject = models.CharField(max_length=20)
    topic = models.CharField(max_length=80)
    title = models.TextField()
    answer = models.CharField(max_length=500)
    alternatives = ArrayField(models.CharField(max_length=500), size=5)


class Exam(models.Model):
    questions = models.ManyToManyField(Question)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_answers = models.JSONField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    score = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(0)], null=True
    )
