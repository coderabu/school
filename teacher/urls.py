from django.urls import path
from .views import TeacherDashboard, TeacherProfile, TeacherGroupDetail, TeacherStudentList, MarkAttendance

app_name = 'teacher'

urlpatterns = [
    path('teacher_page/', TeacherDashboard.as_view(), name='teacher_page'),
    path('group/<int:pk>/', TeacherGroupDetail.as_view(), name='group_detail'),
    path('teacher_profile/', TeacherProfile.as_view(), name='profile'),
    path('teacher_student/', TeacherStudentList.as_view(), name='student_list'),
    path('attendance/', MarkAttendance.as_view(), name='mark_attendance'),
]