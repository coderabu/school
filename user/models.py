from django.db import models

class User(models.Model):
    ROLE = (
        ('ceo','Ceo'),
        ('teacher','Teacher'),
        ('student','Student'),
        ('user','User')
    )

    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=10000)
    role = models.CharField(max_length=20, choices=ROLE, default='user')

