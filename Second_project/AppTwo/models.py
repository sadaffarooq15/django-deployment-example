from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    Email = models.EmailField( max_length=254, unique=True)
    
    