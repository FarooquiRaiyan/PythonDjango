from django.db import models

# Create your models here.

class NewsAdd(models.Model):
    title =models.TextField()
    content= models.TextField()
    