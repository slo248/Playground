from django.db import models

# Create your models here.
class Booking(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
