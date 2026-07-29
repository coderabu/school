from django.urls import path
from .views import (SubjectListView,AddSubjectView,GroupListView,
GroupDetailView,AddGroupView,
DeleteGroupView,AddStudentToGroupView
                    )


app_name = 'groups'

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/add/',AddSubjectView.as_view(), name='add_subject'),

    path('cseo/groups_list/', GroupListView.as_view(), name='group_list'),
    path('add/', AddGroupView.as_view(), name='add_groups'),
    path('<int:pk>/',GroupDetailView.as_view(), name='group_detail'),
    path('<int:pk>/delete/',DeleteGroupView.as_view(), name='delete_group'),
    path('<int:pk>/add-student/', AddStudentToGroupView.as_view(), name='add_student_group'),
]