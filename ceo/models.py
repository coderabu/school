from django.db import models
from user.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_created=True)

class Group(models.Model):
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateField(auto_created=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = models.DateField()

class GroupStudent(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateField()

class Paymet(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    paymet_data = models.DateField()
    for_month = models.CharField(max_length=100)
    paymet_tayp = models.CharField(max_length=100)

class Salary(models.Model):
    paymet_id = models.ForeignKey(Paymet, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)
    salary_data = models.DateField()
    for_month = models.CharField(max_length=100)
    salary_type = models.CharField(max_length=100)

class Attendance(models.Model):
    Status = (
        ('present','Present'),
        ('absent','Absent'),
        ('none','None')
    )

    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=Status, default='none')