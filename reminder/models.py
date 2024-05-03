from django.db import models

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    dated = models.DateField(auto_now_add = True)


   
    