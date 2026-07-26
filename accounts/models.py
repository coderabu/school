from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE = (
        ('ceo','Ceo'),
        ('teacher','Teacher'),
        ('student','Student'),
        ('none','none')
    )
    phone = models.CharField(max_length=55)
    role = models.CharField(max_length=20, choices=ROLE, default='student')
