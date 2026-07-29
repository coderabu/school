from django.urls import path
from .views import (main_page,
    LoginView, teacher_list,TeacherDetailView,
    AddUserView,UpdateTeacher,DeleteTeacher
)
from .views import student_list,StudentDetail,DeleteStudent,UpdateStudent

app_name = 'accounts'
urlpatterns = [
    path('', main_page, name='main_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/<int:pk>/update/', UpdateTeacher.as_view(), name='update_teacher'),
    path('teacher/delete/<int:pk>/', DeleteTeacher.as_view(), name='delete_teacher'),
    path('users/add/', AddUserView.as_view(), name='add_user'),



    path('ceo/student_page/', student_list, name='student'),
    path('ceo/student_detail<int:pk>/',StudentDetail.as_view(),name='student_detail'),
    path('ceo/update_student<int:pk>/',UpdateStudent.as_view(),name='edit_student'),
    path('ceo/delete_student<int:pk>/',DeleteStudent.as_view(),name='delete_student')
]