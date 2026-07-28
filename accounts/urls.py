from django.urls import path
from .views import (main_page,
    LoginView, teacher_list,TeacherDetailView,
    AddUserView,UpdateTeacher,DeleteTeacher
)
from .views import student_list

app_name = 'accounts'
urlpatterns = [
    path('', main_page, name='main_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/<int:pk>/update/', UpdateTeacher.as_view(), name='update_teacher'),
    path('users/add/', AddUserView.as_view(), name='add_user'),
    # path('students/', StudentView.as_view(), name='student_page'),
    path('teacher/delete/<int:pk>/', DeleteTeacher.as_view(), name='delete_teacher'),
    path('accounts/student/', student_list, name='student')
]