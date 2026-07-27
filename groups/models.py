from django.db import models
from accounts.models import User

class Subject(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateField(auto_now=True)

class Groups(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_groups')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    created_at = models.DateField(auto_created=True)
    start_time = models.DateField(auto_created=False)
    end_time = models.DateField(auto_created=False)
    days = models.CharField(max_length=55)

class GroupStudent(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(Groups,on_delete=models.CASCADE)
    created_at = models.DateField(auto_created=True)

