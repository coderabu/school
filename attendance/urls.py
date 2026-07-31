from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.AttendanceGroupList.as_view(), name='group_list'),
    path('group/<int:pk>/', views.AttendanceGroupDetail.as_view(), name='group_detail'),
    path('group/<int:group_pk>/student/<int:student_pk>/', views.AttendanceStudentDetail.as_view(), name='student_detail'),
]