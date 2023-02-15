from django.urls import path

from accounts.views import (
    SignUpView,
    StudentSignUpView,
    TeacherSignUpView,
    StudentDetailView,
    StudentUpdateView,
    StudentDeleteView,
    TeacherDetailView,
    TeacherUpdateView,
    TeacherDeleteView,
    UserDetailView,
    UserListView,
)


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/student/", StudentSignUpView.as_view(), name="student-signup"),
    path("signup/teacher/", TeacherSignUpView.as_view(), name="teacher-signup"),
    path("users/", UserListView.as_view(), name="users"),
    path("user/<int:pk>/detail/", UserDetailView.as_view(), name="user-detail"),
    path(
        "profile/<int:pk>/student/", StudentDetailView.as_view(), name="student-profile"
    ),
    path(
        "update/<int:pk>/student/", StudentUpdateView.as_view(), name="student-update"
    ),
    path(
        "delete/<int:pk>/student/", StudentDeleteView.as_view(), name="student-delete"
    ),
    path(
        "profile/<int:pk>/teacher/", TeacherDetailView.as_view(), name="teacher-profile"
    ),
    path(
        "update/<int:pk>/teacher/", TeacherUpdateView.as_view(), name="teacher-update"
    ),
    path(
        "delete/<int:pk>/teacher/", TeacherDeleteView.as_view(), name="teacher-delete"
    ),
]
