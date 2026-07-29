from django import forms
from django.contrib.auth import get_user_model

from .models import Groups, Subject, GroupStudent

User = get_user_model()


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name',)


class GroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ('name','teacher', 'subject', 'days', 'start_time', 'end_time')


class AddStudentToGroupForm(forms.ModelForm):
    class Meta:
        model = GroupStudent
        fields = ('student',)
