from django.conf import settings
from django.db import models


class Salary(models.Model):
    TYPE_CHOICES = (
        ('cash', 'Cash'),
        ('card', 'Card'),
    )

    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    for_month = models.DateField()
    salary_date = models.DateField(auto_now_add=True)
    salary_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='cash')

    def __str__(self):
        return f"{self.teacher.username} - {self.for_month.strftime('%Y-%m')} - {self.amount}"


class Payment(models.Model):
    TYPE_CHOICES = (
        ('cash', 'Cash'),
        ('card', 'Card'),
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    for_month = models.DateField()
    payment_date = models.DateField(auto_now_add=True)
    payment_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='cash')


    def __str__(self):
        return f"{self.student.username} - {self.for_month.strftime('%Y-%m')} - {self.amount}"