from django.db import models

# Create your models here.
class Visitor(models.Model):

    GENDER_CHOICES = (
        ('Male' , 'Male'),
        ('Female' , 'Female'),
        ('Other' , ('Other'))
    )
    userName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(max_length = 6, choices=GENDER_CHOICES)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=11)
    address = models.TextField()
    password = models.CharField(max_length=100)
    confirmPassword = models.CharField(max_length=100)

def __str__(self):
    return self.userName
