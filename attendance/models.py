from django.db import models
from django.conf import settings
from groups.models import Groups


class Attendance(models.Model):
    Status = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=55, choices=Status)

    class Meta:
        unique_together = ('student', 'group', 'date')

    def __str__(self):
        return f"{self.student.username} - {self.date} - {self.status}"