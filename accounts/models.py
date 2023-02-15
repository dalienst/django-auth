from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("user-detail", args=[str(self.id)])


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(
        max_length=200,
    )

    def get_absolute_url(self):
        return reverse("student-profile", args=[str(self.id)])

    def __str__(self) -> str:
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(
        max_length=200,
    )
    degree = models.CharField(
        max_length=200,
    )

    def get_absolute_url(self):
        return reverse("teacher-profile", args=[str(self.id)])

    def __str__(self) -> str:
        return self.user.username
