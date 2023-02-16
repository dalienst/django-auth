from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Student, Teacher
from django.db import transaction


class StudentSignUpForm(UserCreationForm):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Your email",
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Your email",
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        return user
