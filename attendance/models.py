from django.db import models
from accounts.models import User
from groups.models import Groups

class Attendance(models.Model):
    Status = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=55, choices=Status)
    