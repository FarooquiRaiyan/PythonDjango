from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    roll= models.IntegerField()
    fav_sub = models.CharField(max_length=100)