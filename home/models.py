from django.db import models

# Create your models here.
# each field  is specified as a class attribute and each attribute is the tables column 
class Student(models.Model):
   
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    email=models.EmailField()
    marks=models.IntegerField()
    address=models.CharField(max_length=100)
    image=models.ImageField(null=True)
    file=models.FileField()

# creating the prouduct schema 
class Product(models.Model):
    pass