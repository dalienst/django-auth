from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from accounts.models import User, Student, Teacher
from accounts.forms import StudentSignUpForm, TeacherSignUpForm
from django.contrib.auth import login
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)


class SignUpView(TemplateView):
    template_name = "registration/signup.html"


class UserListView(UserPassesTestMixin, generic.ListView):
    """admin sees all users"""

    model = User
    template_name = "users_list.html"
    paginate_by = 6

    def test_func(self):
        return self.request.user.is_staff


class UserDetailView(UserPassesTestMixin, generic.DetailView):
    """details on specific users"""

    model = User
    template_name = "user_detail.html"

    def test_func(self):
        return self.request.user.is_staff


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    """View the details of the student"""

    model = Student
    template_name = "student_profile.html"


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    """student updates their profile"""

    model = Student
    fields = [
        "location",
    ]
    template_name = "student_update.html"
    success_url = reverse_lazy("home")


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    """student deletes their profile"""

    model = Student
    template_name = "student_delete.html"
    success_url = reverse_lazy("signup")


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "teacher"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class TeacherDetailView(LoginRequiredMixin, generic.DetailView):
    """Teacher views their details"""

    model = Teacher
    template_name = "teacher_profile.html"


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    """Teacher updates profile"""

    model = Teacher
    fields = ["location", "degree"]
    template_name = "teacher_update.html"
    success_url = reverse_lazy("home")


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    """Teacher deletes their profile"""

    model = Teacher
    template_name = "teacher_delete.html"
    success_url = reverse_lazy("signup")
